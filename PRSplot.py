# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:23:31 2026

@author: peter
"""

import numpy as np
import matplotlib as mpl
import pylab
import warnings
warnings.filterwarnings('ignore')
np.set_printoptions(precision = 3)


def npm(ndarray1, ndarray2):
    return np.multiply(ndarray1, ndarray2)


class PlotPRS():
    def __init__(self,PRSx,D):
        """
        Plot PRS objects.
        
        Parameters
        ----------
        PRSx: PRS.PRS() object
            PRS to plot
        D: array, in mm
            1e3 times self.D[idx] from PRSgamma input.
        """
        self.PRSx = PRSx
        self.D = D
        self.c = mpl.cm.get_cmap('viridis')
        pylab.rcParams['font.size'] = 14
    
    def NofD(self,logN0,mu,la):
        """
        Calculate size distribution N(D) for gamma fit parameters N0, mu, lambda.

        Args:
            logN0: Values of log10(N0).
            mu: Values of mu.
            la: Values of lambda.
        
        Returns:
            Size distribution N(D) in m^-3 mm^-1 for gamma fit parameters N0, mu, lambda.
        """
        return 1e-3*npm(npm(10**logN0,np.power(0.1*self.D,mu)),np.exp(-npm(0.1*self.D,10*la)))

    def VertexFit(self,ax):
        """
        Plots N(D) for the vertices and most likely solution of a PRS.
        
        Args:
            ax: Plot axes.
        """
        [mu_m1,mu_l1,mu_u1,la_m1,la_lm1,la_um1,la_l1,la_u1,logN0_m1,logN0_lm1,
         logN0_um1,logN0_ll1,logN0_ul1,logN0_l1,logN0_u1] = self.PRSx.Vertex()
        ax.loglog(self.D,self.NofD(logN0_m1,mu_m1,la_m1),color='k',lw=3,
                     label=r"ML (most likely)")
        ax.loglog(self.D,self.NofD(logN0_l1,mu_m1,la_m1),'--',color=self.c(0.0),lw=2,
                     label=r"$N_0 < N_{0,ML}$ (lighter)")
        ax.loglog(self.D,self.NofD(logN0_u1,mu_m1,la_m1),color=self.c(0.0),lw=2,
                     label=r"$N_0 > N_{0,ML}$ (heavier)")
        ax.loglog(self.D,self.NofD(logN0_lm1,mu_l1,la_lm1),'--',color=self.c(0.8),lw=2,zorder=2.5,
                     label=r"$\mu < \mu_{ML}$ (broader PSD)")
        ax.loglog(self.D,self.NofD(logN0_um1,mu_u1,la_um1),color=self.c(0.8),lw=2,zorder=2.5,
                     label=r"$\mu > \mu_{ML}$ (narrower PSD)")
        ax.loglog(self.D,self.NofD(logN0_ll1,mu_m1,la_l1),'--',color=self.c(0.4),lw=2,zorder=2.25,
                     label=r"$\lambda < \lambda_{ML}$ (larger MMD)")
        ax.loglog(self.D,self.NofD(logN0_ul1,mu_m1,la_u1),color=self.c(0.4),lw=2,zorder=2.25,
                     label=r"$\lambda > \lambda_{ML}$ (smaller MMD)")
        ax.set_title(r'Gamma Fits to $N$($D$) vs. $D$')
        ax.set_xlabel(r'$D$ [mm]')
        ax.set_ylabel(r'$N$($D$) [m$^{-3}$ mm$^{-1}$]')
        ax.legend(fontsize=12)
        ax.set_xlim(1e-1,5e1)
        ax.set_ylim(1e1,1e6)
        
    def VertexFitA(self,ax):
        """
        Plots N(D) for the most likely solution of a PRS.
        
        Args:
            ax: Plot axes.
        """
        [mu_m1,mu_l1,mu_u1,la_m1,la_lm1,la_um1,la_l1,la_u1,logN0_m1,logN0_lm1,
         logN0_um1,logN0_ll1,logN0_ul1,logN0_l1,logN0_u1] = self.PRSx.Vertex()
        ax.loglog(self.D,self.NofD(logN0_m1,mu_m1,la_m1),color='k',lw=3,
                     label=r"ML (most likely)")
        ax.set_title(r'Gamma Fits to $N$($D$) vs. $D$')
        ax.set_xlabel(r'$D$ [mm]')
        ax.set_ylabel(r'$N$($D$) [m$^{-3}$ mm$^{-1}$]')
        ax.legend(fontsize=12)
        ax.set_xlim(1e-1,2e1)
        ax.set_ylim(1e1,1e5)
    
    def VertexFitB(self,ax):
        """
        Plots N(D) for the vertices in mu and most likely solution of a PRS.
        
        Args:
            ax: Plot axes.
        """
        [mu_m1,mu_l1,mu_u1,la_m1,la_lm1,la_um1,la_l1,la_u1,logN0_m1,logN0_lm1,
         logN0_um1,logN0_ll1,logN0_ul1,logN0_l1,logN0_u1] = self.PRSx.Vertex()
        ax.loglog(self.D,self.NofD(logN0_m1,mu_m1,la_m1),color='k',lw=3,
                     label=r"ML (most likely)")
        ax.loglog(self.D,self.NofD(logN0_lm1,mu_l1,la_lm1),'--',color=self.c(0.4),lw=2,zorder=2.5,
                     label=r"$\mu < \mu_{ML}$ (broader)")
        ax.loglog(self.D,self.NofD(logN0_um1,mu_u1,la_um1),color=self.c(0.4),lw=2,zorder=2.5,
                     label=r"$\mu > \mu_{ML}$ (narrower)")
        ax.set_title(r'Gamma Fits to $N$($D$) vs. $D$')
        ax.set_xlabel(r'$D$ [mm]')
        ax.set_ylabel(r'$N$($D$) [m$^{-3}$ mm$^{-1}$]')
        ax.legend(fontsize=12)
        ax.set_xlim(1e-1,2e1)
        ax.set_ylim(1e1,1e5)
        
    def VertexFitC(self,ax):
        """
        Plots N(D) for the vertices in lambda and most likely solution of a PRS.
        
        Args:
            ax: Plot axes.
        """
        [mu_m1,mu_l1,mu_u1,la_m1,la_lm1,la_um1,la_l1,la_u1,logN0_m1,logN0_lm1,
         logN0_um1,logN0_ll1,logN0_ul1,logN0_l1,logN0_u1] = self.PRSx.Vertex()
        ax.loglog(self.D,self.NofD(logN0_m1,mu_m1,la_m1),color='k',lw=3,
                     label=r"ML (most likely)")
        ax.loglog(self.D,self.NofD(logN0_ll1,mu_m1,la_l1),'--',color=self.c(0.4),lw=2,zorder=2.25,
                     label=r"$\lambda < \lambda_{ML}$ (larger $D$)")
        ax.loglog(self.D,self.NofD(logN0_ul1,mu_m1,la_u1),color=self.c(0.4),lw=2,zorder=2.25,
                     label=r"$\lambda > \lambda_{ML}$ (smaller $D$)")
        ax.set_title(r'Gamma Fits to $N$($D$) vs. $D$')
        ax.set_xlabel(r'$D$ [mm]')
        ax.set_ylabel(r'$N$($D$) [m$^{-3}$ mm$^{-1}$]')
        ax.legend(fontsize=12)
        ax.set_xlim(1e-1,2e1)
        ax.set_ylim(1e1,1e5)
    
    def VertexFitD(self,ax):
        """
        Plots N(D) for the vertices in N0 and most likely solution of a PRS.
        
        Args:
            ax: Plot axes.
        """
        [mu_m1,mu_l1,mu_u1,la_m1,la_lm1,la_um1,la_l1,la_u1,logN0_m1,logN0_lm1,
         logN0_um1,logN0_ll1,logN0_ul1,logN0_l1,logN0_u1] = self.PRSx.Vertex()
        ax.loglog(self.D,self.NofD(logN0_m1,mu_m1,la_m1),color='k',lw=3,
                     label=r"ML (most likely)")
        ax.loglog(self.D,self.NofD(logN0_l1,mu_m1,la_m1),'--',color=self.c(0.4),lw=2,
                     label=r"$N_0 < N_{0,ML}$ (lighter)")
        ax.loglog(self.D,self.NofD(logN0_u1,mu_m1,la_m1),color=self.c(0.4),lw=2,
                     label=r"$N_0 > N_{0,ML}$ (heavier)")
        ax.set_title(r'Gamma Fits to $N$($D$) vs. $D$')
        ax.set_xlabel(r'$D$ [mm]')
        ax.set_ylabel(r'$N$($D$) [m$^{-3}$ mm$^{-1}$]')
        ax.legend(fontsize=12)
        ax.set_xlim(1e-1,2e1)
        ax.set_ylim(1e1,1e5)

    def VertexFitSingle(self,ax):
        """
        Plots N(D) for the vertices and most likely solution of a single PRS.
        
        Args:
            ax: Plot axes.
        """
        [mu_m1,mu_l1,mu_u1,la_m1,la_lm1,la_um1,la_l1,la_u1,logN0_m1,logN0_lm1,
         logN0_um1,logN0_ll1,logN0_ul1,logN0_l1,logN0_u1] = self.PRSx.Vertex()
        ax.loglog(self.D,self.NofD(logN0_m1,mu_m1,la_m1),color=self.c(0.8),lw=2,zorder=2.25)
        ax.loglog(self.D,self.NofD(logN0_l1,mu_m1,la_m1),color=self.c(0.8),lw=2,zorder=2.25)
        ax.loglog(self.D,self.NofD(logN0_u1,mu_m1,la_m1),color=self.c(0.8),lw=2,zorder=2.25)
        ax.loglog(self.D,self.NofD(logN0_lm1,mu_l1,la_lm1),color=self.c(0.8),lw=2,zorder=2.25)
        ax.loglog(self.D,self.NofD(logN0_um1,mu_u1,la_um1),color=self.c(0.8),lw=2,zorder=2.25)
        ax.loglog(self.D,self.NofD(logN0_ll1,mu_m1,la_l1),color=self.c(0.8),lw=2,zorder=2.25)
        ax.loglog(self.D,self.NofD(logN0_ul1,mu_m1,la_u1),color=self.c(0.8),lw=2,zorder=2.25)
        ax.set_xlabel(r'$D$ [mm]')
        ax.set_ylabel(r'$N$($D$) [m$^{-3}$ mm$^{-1}$]')
        ax.set_xlim(1e-1,2e1)
        ax.set_ylim(1e1,1e5)

    def VolCrossCompare(self,ax,color,lgdx):
        """
        Plots features of a PRS for illustration.
                
        Args:
            ax: Plot axes.
            color: Color used for PRS graphic.
            lgdx: Legend entry.
        """
        var = self.PRSx.Plot(ax,color)
        y = var[0]
        z = var[1]
        y2 = var[2]
        z2l = var[3]
        z2u = var[4]
        z2a = z2l[np.where(np.abs(y2-y) == np.min(np.abs(y2-y)))]
        z2b = z2u[np.where(np.abs(y2-y) == np.min(np.abs(y2-y)))]
        ax.scatter(y,z,25,color=[0,0,0],zorder=2.5)
        ax.scatter(-2,-1,25,color=color,label=lgdx) # dummy point for legend
        ax.vlines(y,z2a,z2b,color='k')
        ax.plot(y2,np.sqrt(npm(z2l,z2u)),color=self.c(1.0))

    def VolCrossProjection(self,ax,jumpup=True):
        """
        Projects the surface of a 3D PRS onto the mu-lambda axes. Fill color varies with N0.
        Opposite quarters of the 3D surface are projected onto top and bottom halves of the 
        cross-section to visualize the thickness of the 3D PRS.
        
        Args:
            ax: Plot axes.
            jumpup: Boolean, optional
                If True, projection of N0 onto mu-lambda cross-section jumps up 
                as lambda increases across its most likely value.
                If False, projection of N0 onto mu-lambda cross-section jumps down 
                as lambda increases across its most likely value.
        
        Returns:
            cax: Mappable for colormap.
        """
        var = self.PRSx.PRS(jumpup)
        y = var[1]
        z = var[2]
        X = var[3]
        Y = var[4]
        Z = var[5]
        ax.scatter(y,z,25,color=[1,1,1],zorder=2.5)
        cax = ax.scatter(Y,Z,self.PRSx.chisq,c=X)
        ax.set_xlim(left=-1)
        ax.set_ylim(bottom=0)
        ax.set_xlabel(r"$\mu$")
        ax.set_ylabel(r"$\lambda$ [mm$^{-1}$]")
        return cax
    
    def VolCrossSingle(self,ax,color):
        """
        Like VolCrossCompare, but initializes figure and adds a fill color that varies with N0.
        
        Args:
            ax: Plot axes.
            color: Color used for PRS graphic.
            
        Returns:
            cax: Mappable for colormap.
        """
        var = self.PRSx.Plot(ax,color,False,True)
        y = var[0]
        z = var[1]
        y2 = var[2]
        z2l = var[3]
        z2u = var[4]
        X = var[5]
        Y = var[6]
        Z = var[7]
        z2a = z2l[np.where(np.abs(y2-y) == np.min(np.abs(y2-y)))]
        z2b = z2u[np.where(np.abs(y2-y) == np.min(np.abs(y2-y)))]
        ax.scatter(y,z,25,color=[1,1,1],zorder=2.5)
        ax.vlines(y,z2a,z2b,color=self.c(0.9))
        ax.plot(y2,np.sqrt(npm(z2l,z2u)),color=[0,0,0])
        cax = ax.scatter(Y,Z,self.PRSx.chisq,c=X)
        ax.set_xlim(left=-1)
        ax.set_ylim(bottom=0)
        ax.set_xlabel(r"$\mu$")
        ax.set_ylabel(r"$\lambda$ [mm$^{-1}$]")
        return cax