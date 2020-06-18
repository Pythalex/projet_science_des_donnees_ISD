import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.integrate import odeint

class SEIRModel():
    """
    Cette classe représente une modélisation SEIR épidémiologique.
    Les paramètres du modèles sont beta, gamma et delta dont les valeurs initiales sont données à
    l'instanciation de la classe.
    
    beta = taux de contact en personnes / jours (vitesse de la propagation de la maladie)
    gamma = moyenne de temps de guérison en 1 / jours (vitesse de guérison de la maladie)
    delta = temps d'incubation (jours après lequel un Exposed devient Infected)
    """
    def __init__(self, beta_init=0.1, gamma_init=0.3, delta_init=14, R0=0, I0=1, N=67000000, E0=0):
        self.beta_0 = beta_init
        self.gamma_0 = gamma_init
        self.delta_0 = delta_init
        self.beta_ = None
        self.gamma_ = None
        self.delta_ = None
        # Total population, N.
        self.N = N
        # Initial number of infected and recovered individuals, I0 and R0.
        self.I0, self.R0 = I0, R0
        # Initial number of exposed (infected not contagious)
        self.E0 = E0
        # Everyone else, S0, is susceptible to infection initially.
        self.S0 = self.N - self.I0 - self.R0 - self.E0

    def fit(self, X, y):
        """
        Ajuste les paramètres beta et gamma du modèle sur le jeu de données d'entrée.
        
        Returns:
            self for method chaining.
        """
        self.beta_ = self.beta_0
        self.gamma_ = self.gamma_0
        self.delta_ = self.delta_0
        
        # Initial conditions vector
        y0 = self.S0, self.E0, self.I0, self.R0
        
        f = lambda t, beta, gamma, delta : (odeint(self.deriv, y0, t, args=(self.N, 
                                                                     beta, 
                                                                     gamma,
                                                                     delta)).T)[2] # [2] = only Infected
        params, covariance = scipy.optimize.curve_fit(f, X, y) # fit
        self.beta_, self.gamma_, self.delta_ = params
        
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
        y0 = self.S0, self.E0, self.I0, self.R0
        
        # Integrate the SIR equations over the time grid, t.
        ret = odeint(self.deriv, y0, t, args=(self.N, self.beta_, self.gamma_, self.delta_))
        S, E, I, R = ret.T
            
        return S, E, I, R
    
    
    def deriv(self, y, t, N, beta, gamma, delta):
        S, E, I, _ = y
        dSdt = -beta * S * I / N
        dEdt = beta * S * I / N - delta * E
        dIdt = delta * E - gamma * I
        dRdt = gamma * I
        return dSdt, dEdt, dIdt, dRdt