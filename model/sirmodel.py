import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import odeint

class SIRModel():
    """
    Cette classe représente une modélisation SIR épidémiologique.
    Les paramètres du modèles sont beta et gamma dont les valeurs initiales sont données à
    l'instanciation de la classe.
    
    beta = taux de contact (vitesse de la propagation de la maladie)
    gamma = moyenne de temps de guérison (vitesse de guérison de la maladie)
    """
    def __init__(self, beta_init=0.1, gamma_init=0.3, R0=0, I0=3, N=67000000):
        self.beta_0 = beta_init
        self.gamma_0 = gamma_init
        self.beta_ = None
        self.gamma_ = None
        # Total population, N.
        self.N = N
        # Initial number of infected and recovered individuals, I0 and R0.
        self.I0, self.R0 = I0, R0
        # Everyone else, S0, is susceptible to infection initially.
        self.S0 = self.N - self.I0 - self.R0

    def fit(self, X, y):
        """
        Ajuste les paramètres beta et gamma du modèle sur le jeu de données d'entrée.
        
        Returns:
            self for method chaining.
        """
        self.beta_ = self.beta_0
        self.gamma_ = self.gamma_0
        
        # Initial conditions vector
        y0 = self.S0, self.I0, self.R0
        
        f = lambda t, beta, gamma : (odeint(self.deriv, y0, t, args=(self.N, 
                                                                     beta, 
                                                                     gamma)).T)[1] # [1] = only Infected
        params, covariance = scipy.optimize.curve_fit(f, X, y) # fit
        self.beta_, self.gamma_ = params
        
        print(params)
        
        return self


    def predict(self, t):
        """
        Predict the S I R values for given time
        TODO : defines values
        """
        if self.beta_ is None or self.gamma_ is None:
            raise Exception("SIRModel not fitted")
            
        # Initial conditions vector
        y0 = self.S0, self.I0, self.R0
        
        # Integrate the SIR equations over the time grid, t.
        ret = odeint(self.deriv, y0, t, args=(self.N, self.beta_, self.gamma_))
        S, I, R = ret.T
            
        return S, I, R
    
    
    def deriv(self, y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt