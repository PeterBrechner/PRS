# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 15:23:31 2026

@author: peter
"""

import numpy as np
import matplotlib as mpl
import pylab
import json
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
np.set_printoptions(precision = 3)


def npm(ndarray1, ndarray2):
    return np.multiply(ndarray1, ndarray2)

def npd(ndarray1, ndarray2):
    return np.divide(ndarray1, ndarray2)


class PlotPRS():
    def __init__(self,PRS1,PRS2,PRS3,PRS4,PRS5,PRS6,dirr,lgdx,catx,name):
        """
        Plot PRS objects for three quantitative regimes (e.g., colder, moderate, warmer)
        in two categorical regimes (e.g., ice phase, mixed phase).
        
        Parameters
        ----------
        PRS1: PRS.PRS() object
            PRS for first quantitative regime and first categorical regime.
        PRS2: PRS.PRS() object
            PRS for second quantitative regime and first categorical regime.
        PRS3: PRS.PRS() object
            PRS for third quantitative regime and first categorical regime.
        PRS4: PRS.PRS() object
            PRS for first quantitative regime and second categorical regime.
        PRS5: PRS.PRS() object
            PRS for second quantitative regime and second categorical regime.
        PRS6: PRS.PRS() object
            PRS for third quantitative regime and second categorical regime.
        dirr: str
            Table directory.
        lgdx: list
            Legend for quantitative regimes.
        catx: list
            Legend for categorical regimes.
        name: str
            Name used in tables.
        """
        self.PRS1 = PRS1
        self.PRS2 = PRS2
        self.PRS3 = PRS3
        self.PRS4 = PRS4
        self.PRS5 = PRS5
        self.PRS6 = PRS6
        self.dirr = dirr
        self.lgdx = lgdx
        self.catx = catx
        self.name = name
        self.c = mpl.cm.get_cmap('viridis')
        pylab.rcParams['font.size'] = 14
    
    def BC(self,res=21):
        """
        Create tables of Bhattacharyya coefficients for each pair of PRSs.
        
        Args:
            res: Grid resolution for numerical integration. Default is 21.
        """
        #Note: For common coordinates, PRSs must be normalized.
        PRSa = [self.PRS1,self.PRS2,self.PRS3,self.PRS4,self.PRS5,self.PRS6]
        BCxyz = np.zeros((6,6))
        BCy = np.zeros((6,6))
        BCyz = np.zeros((6,6))
        for i in range(6):
            for j in range(6):
                BCxyz[i,j] = self.CalcBCxyz(PRSa[i],PRSa[j],res)
                BCy[i,j] = self.CalcBCy(PRSa[i],PRSa[j])
                BCyz[i,j] = self.CalcBCyz(PRSa[i],PRSa[j],res)
        BCx = npd(BCxyz,BCyz)
        BCz = npd(BCyz,BCy)
        lg = self.lgdx
        ct = self.catx
        lgd = [lg[0]+", "+ct[0],lg[1]+", "+ct[0],lg[2]+", "+ct[0],lg[0]+", "+ct[1],lg[1]+", "+ct[1],lg[2]+", "+ct[1]]
        
        BC = BCxyz
        data = {lgd[0]:[np.round(BC[0,0],3),np.round(BC[0,1],3),np.round(BC[0,2],3),np.round(BC[0,3],3),np.round(BC[0,4],3),np.round(BC[0,5],3)],
                lgd[1]:[np.round(BC[1,0],3),np.round(BC[1,1],3),np.round(BC[1,2],3),np.round(BC[1,3],3),np.round(BC[1,4],3),np.round(BC[1,5],3)],
                lgd[2]:[np.round(BC[2,0],3),np.round(BC[2,1],3),np.round(BC[2,2],3),np.round(BC[2,3],3),np.round(BC[2,4],3),np.round(BC[2,5],3)],
                lgd[3]:[np.round(BC[3,0],3),np.round(BC[3,1],3),np.round(BC[3,2],3),np.round(BC[3,3],3),np.round(BC[3,4],3),np.round(BC[3,5],3)],
                lgd[4]:[np.round(BC[4,0],3),np.round(BC[4,1],3),np.round(BC[4,2],3),np.round(BC[4,3],3),np.round(BC[4,4],3),np.round(BC[4,5],3)],
                lgd[5]:[np.round(BC[5,0],3),np.round(BC[5,1],3),np.round(BC[5,2],3),np.round(BC[5,3],3),np.round(BC[5,4],3),np.round(BC[5,5],3)]}
        df = pd.DataFrame(data,index=lgd)
        df.to_excel(self.dirr+'Bhattacharyya_3D'+self.name+'.xlsx')
        
        BC = BCyz
        data = {lgd[0]:[np.round(BC[0,0],3),np.round(BC[0,1],3),np.round(BC[0,2],3),np.round(BC[0,3],3),np.round(BC[0,4],3),np.round(BC[0,5],3)],
                lgd[1]:[np.round(BC[1,0],3),np.round(BC[1,1],3),np.round(BC[1,2],3),np.round(BC[1,3],3),np.round(BC[1,4],3),np.round(BC[1,5],3)],
                lgd[2]:[np.round(BC[2,0],3),np.round(BC[2,1],3),np.round(BC[2,2],3),np.round(BC[2,3],3),np.round(BC[2,4],3),np.round(BC[2,5],3)],
                lgd[3]:[np.round(BC[3,0],3),np.round(BC[3,1],3),np.round(BC[3,2],3),np.round(BC[3,3],3),np.round(BC[3,4],3),np.round(BC[3,5],3)],
                lgd[4]:[np.round(BC[4,0],3),np.round(BC[4,1],3),np.round(BC[4,2],3),np.round(BC[4,3],3),np.round(BC[4,4],3),np.round(BC[4,5],3)],
                lgd[5]:[np.round(BC[5,0],3),np.round(BC[5,1],3),np.round(BC[5,2],3),np.round(BC[5,3],3),np.round(BC[5,4],3),np.round(BC[5,5],3)]}
        df = pd.DataFrame(data,index=lgd)
        df.to_excel(self.dirr+'Bhattacharyya_2D'+self.name+'.xlsx')
        
        BC = BCx
        data = {lgd[0]:[np.round(BC[0,0],3),np.round(BC[0,1],3),np.round(BC[0,2],3),np.round(BC[0,3],3),np.round(BC[0,4],3),np.round(BC[0,5],3)],
                lgd[1]:[np.round(BC[1,0],3),np.round(BC[1,1],3),np.round(BC[1,2],3),np.round(BC[1,3],3),np.round(BC[1,4],3),np.round(BC[1,5],3)],
                lgd[2]:[np.round(BC[2,0],3),np.round(BC[2,1],3),np.round(BC[2,2],3),np.round(BC[2,3],3),np.round(BC[2,4],3),np.round(BC[2,5],3)],
                lgd[3]:[np.round(BC[3,0],3),np.round(BC[3,1],3),np.round(BC[3,2],3),np.round(BC[3,3],3),np.round(BC[3,4],3),np.round(BC[3,5],3)],
                lgd[4]:[np.round(BC[4,0],3),np.round(BC[4,1],3),np.round(BC[4,2],3),np.round(BC[4,3],3),np.round(BC[4,4],3),np.round(BC[4,5],3)],
                lgd[5]:[np.round(BC[5,0],3),np.round(BC[5,1],3),np.round(BC[5,2],3),np.round(BC[5,3],3),np.round(BC[5,4],3),np.round(BC[5,5],3)]}
        df = pd.DataFrame(data,index=lgd)
        df.to_excel(self.dirr+'Bhattacharyya_N0'+self.name+'.xlsx')
        
        BC = BCy
        data = {lgd[0]:[np.round(BC[0,0],3),np.round(BC[0,1],3),np.round(BC[0,2],3),np.round(BC[0,3],3),np.round(BC[0,4],3),np.round(BC[0,5],3)],
                lgd[1]:[np.round(BC[1,0],3),np.round(BC[1,1],3),np.round(BC[1,2],3),np.round(BC[1,3],3),np.round(BC[1,4],3),np.round(BC[1,5],3)],
                lgd[2]:[np.round(BC[2,0],3),np.round(BC[2,1],3),np.round(BC[2,2],3),np.round(BC[2,3],3),np.round(BC[2,4],3),np.round(BC[2,5],3)],
                lgd[3]:[np.round(BC[3,0],3),np.round(BC[3,1],3),np.round(BC[3,2],3),np.round(BC[3,3],3),np.round(BC[3,4],3),np.round(BC[3,5],3)],
                lgd[4]:[np.round(BC[4,0],3),np.round(BC[4,1],3),np.round(BC[4,2],3),np.round(BC[4,3],3),np.round(BC[4,4],3),np.round(BC[4,5],3)],
                lgd[5]:[np.round(BC[5,0],3),np.round(BC[5,1],3),np.round(BC[5,2],3),np.round(BC[5,3],3),np.round(BC[5,4],3),np.round(BC[5,5],3)]}
        df = pd.DataFrame(data,index=lgd)
        df.to_excel(self.dirr+'Bhattacharyya_mu'+self.name+'.xlsx')
        
        BC = BCz
        data = {lgd[0]:[np.round(BC[0,0],3),np.round(BC[0,1],3),np.round(BC[0,2],3),np.round(BC[0,3],3),np.round(BC[0,4],3),np.round(BC[0,5],3)],
                lgd[1]:[np.round(BC[1,0],3),np.round(BC[1,1],3),np.round(BC[1,2],3),np.round(BC[1,3],3),np.round(BC[1,4],3),np.round(BC[1,5],3)],
                lgd[2]:[np.round(BC[2,0],3),np.round(BC[2,1],3),np.round(BC[2,2],3),np.round(BC[2,3],3),np.round(BC[2,4],3),np.round(BC[2,5],3)],
                lgd[3]:[np.round(BC[3,0],3),np.round(BC[3,1],3),np.round(BC[3,2],3),np.round(BC[3,3],3),np.round(BC[3,4],3),np.round(BC[3,5],3)],
                lgd[4]:[np.round(BC[4,0],3),np.round(BC[4,1],3),np.round(BC[4,2],3),np.round(BC[4,3],3),np.round(BC[4,4],3),np.round(BC[4,5],3)],
                lgd[5]:[np.round(BC[5,0],3),np.round(BC[5,1],3),np.round(BC[5,2],3),np.round(BC[5,3],3),np.round(BC[5,4],3),np.round(BC[5,5],3)]}
        df = pd.DataFrame(data,index=lgd)
        df.to_excel(self.dirr+'Bhattacharyya_lambda'+self.name+'.xlsx')
    
    def CalcBCxyz(self,PRS1,PRS2,res=21):
        """
        Calculate the Bhattacharyya coefficient for (N0,mu,lambda) for a pair of PRSs.

        Args:
            PRS1: First PRS
            PRS2: Second PRS
            res: Grid resolution for numerical integration. Default is 21.

        Returns:
            Bhattacharyya coefficient
        """
        
        if (PRS1.norm & PRS2.norm):
            #Use closed form expression for pairs of normalized PRSs. 
            yp = PRS2.ym-PRS1.ym
            zp = PRS2.zm-PRS1.zm
            xp = PRS2.xm-PRS1.xm
            chi2y = 0.5*yp**2/(PRS1.ys**2+PRS2.ys**2)
            chi2z = 0.5*zp**2/(PRS1.zs**2+PRS2.zs**2)
            chi2x = 0.5*xp**2/(PRS1.xs**2+PRS2.xs**2)
            num = np.sqrt((2*PRS1.ys*PRS2.ys)*(2*PRS1.zs*PRS2.zs)*(2*PRS1.xs*PRS2.xs))
            den = np.sqrt((PRS1.ys**2+PRS2.ys**2)*(PRS1.zs**2+PRS2.zs**2)*(PRS1.xs**2+PRS2.xs**2))
            return (num/den)*np.exp(-0.5*(chi2y+chi2z+chi2x))
        else:
            #No closed form expression exists for the general case.
            #Must sum the geometric mean of probability densities over an (x,y,z) grid to estimate the triple integral.
            #Optimize the (x,y,z) grid to minimize numerical error and computational time.
            xm = (PRS1.xm*PRS2.xs**2+PRS2.xm*PRS1.xs**2)/(PRS1.xs**2+PRS2.xs**2)
            ym = (PRS1.ym*PRS2.ys**2+PRS2.ym*PRS1.ys**2)/(PRS1.ys**2+PRS2.ys**2)
            zm = (PRS1.zm*PRS2.zs**2+PRS2.zm*PRS1.zs**2)/(PRS1.zs**2+PRS2.zs**2)
            stdx1 = np.sqrt(PRS1.xs**2+PRS1.b[0]**2*PRS1.zs**2+PRS1.b[1]**2*PRS1.ys**2)
            stdx2 = np.sqrt(PRS2.xs**2+PRS2.b[0]**2*PRS2.zs**2+PRS2.b[1]**2*PRS2.ys**2)
            stdz1 = np.sqrt(PRS1.zs**2+PRS1.a[0]**2*PRS1.ys**2)
            stdz2 = np.sqrt(PRS2.zs**2+PRS2.a[0]**2*PRS2.ys**2)
            x = np.linspace(xm-4*np.sqrt(stdx1*stdx2),xm+4*np.sqrt(stdx1*stdx2),res)
            y = np.linspace(ym-4*np.sqrt(PRS1.ys*PRS2.ys),ym+4*np.sqrt(PRS1.ys*PRS2.ys),res)
            z = np.linspace(zm-4*np.sqrt(stdz1*stdz2),zm+4*np.sqrt(stdz1*stdz2),res)
            #Compute the geometric mean of probability densities at each point on the (x,y,z) grid.
            den = np.sqrt((2*np.pi*PRS1.xs*PRS2.xs)*(2*np.pi*PRS1.ys*PRS2.ys)*(2*np.pi*PRS1.zs*PRS2.zs))
            prob = np.zeros((len(x),len(y),len(z)))
            for i in range(len(x)):
                for j in range(len(y)):
                    for k in range(len(z)):
                        prob[i,j,k] = (1/den)*np.exp(-0.25*(PRS1.chi2x(y[j],z[k],x[i])**2+PRS2.chi2x(y[j],z[k],x[i])**2
                                                            +PRS1.chi2y(y[j])**2+PRS2.chi2y(y[j])**2
                                                            +PRS1.chi2z(y[j],z[k])**2+PRS2.chi2z(y[j],z[k])**2))
            #Multiply the sum of the probability densities by the grid spacing.
            return np.sum(prob)*(x[1]-x[0])*(y[1]-y[0])*(z[1]-z[0])
    
    def CalcBCy(self,PRS1,PRS2):
        """
        Calculate the Bhattacharyya coefficient for mu for a pair of PRSs.

        Args:
            PRS1: First PRS
            PRS2: Second PRS

        Returns:
            Bhattacharyya coefficient for mu
        """
        
        #Use closed form expression for all cases.
        yp = PRS2.ym-PRS1.ym
        chi2y = 0.5*yp**2/(PRS1.ys**2+PRS2.ys**2)
        num = np.sqrt(2*PRS1.ys*PRS2.ys)
        den = np.sqrt(PRS1.ys**2+PRS2.ys**2)
        return (num/den)*np.exp(-0.5*chi2y)
    
    def CalcBCyz(self,PRS1,PRS2,res=21):
        """
        Calculate the Bhattacharyya coefficient for (mu,lambda) for a pair of PRSs.
        The Bhattacharyya coefficient for N0 is CalcBCxyz() divided by this.
        The Bhattacharyya coefficient for lambda is this divided by CalcBCy().

        Args:
            PRS1: First PRS
            PRS2: Second PRS
            res: Grid resolution for numerical integration. Default is 21.

        Returns:
            Bhattacharyya coefficient for (mu,lambda)
        """
        
        if (PRS1.norm & PRS2.norm):
            #Use closed form expression for pairs of normalized PRSs. 
            yp = PRS2.ym-PRS1.ym
            zp = PRS2.zm-PRS1.zm
            chi2y = 0.5*yp**2/(PRS1.ys**2+PRS2.ys**2)
            chi2z = 0.5*zp**2/(PRS1.zs**2+PRS2.zs**2)
            num = np.sqrt((2*PRS1.ys*PRS2.ys)*(2*PRS1.zs*PRS2.zs))
            den = np.sqrt((PRS1.ys**2+PRS2.ys**2)*(PRS1.zs**2+PRS2.zs**2))
            return (num/den)*np.exp(-0.5*(chi2y+chi2z))
        else:
            #No closed form expression exists for the general case.
            #Must sum the geometric mean of probability densities over an (x,y,z) grid to estimate the triple integral.
            #Optimize the (x,y,z) grid to minimize numerical error and computational time.
            ym = (PRS1.ym*PRS2.ys**2+PRS2.ym*PRS1.ys**2)/(PRS1.ys**2+PRS2.ys**2)
            zm = (PRS1.zm*PRS2.zs**2+PRS2.zm*PRS1.zs**2)/(PRS1.zs**2+PRS2.zs**2)
            stdz1 = np.sqrt(PRS1.zs**2+PRS1.a[0]**2*PRS1.ys**2)
            stdz2 = np.sqrt(PRS2.zs**2+PRS2.a[0]**2*PRS2.ys**2)
            y = np.linspace(ym-4*np.sqrt(PRS1.ys*PRS2.ys),ym+4*np.sqrt(PRS1.ys*PRS2.ys),res)
            z = np.linspace(zm-4*np.sqrt(stdz1*stdz2),zm+4*np.sqrt(stdz1*stdz2),res)
            #Compute the geometric mean of probability densities at each point on the (x,y,z) grid.
            den = np.sqrt((2*np.pi*PRS1.ys*PRS2.ys)*(2*np.pi*PRS1.zs*PRS2.zs))
            prob = np.zeros((len(y),len(z)))
            for j in range(len(y)):
                for k in range(len(z)):
                    prob[j,k] = (1/den)*np.exp(-0.25*(PRS1.chi2y(y[j])**2+PRS2.chi2y(y[j])**2
                                                      +PRS1.chi2z(y[j],z[k])**2+PRS2.chi2z(y[j],z[k])**2))
            #Multiply the sum of the probability densities by the grid spacing.
            return np.sum(prob)*(y[1]-y[0])*(z[1]-z[0])
    
    def VertexParams(self,ax):
        """
        Creates table of gamma fit parameters for the vertices and most likely solution of a PRS.
        Outputs linear regression coefficients to JSON file.
        
        Args:
            ax: Plot axes.
        """
        [mu_m1,mu_l1,mu_u1,la_m1,la_lm1,la_um1,la_l1,la_u1,logN0_m1,logN0_lm1,
         logN0_um1,logN0_ll1,logN0_ul1,logN0_l1,logN0_u1] = self.PRS1.Vertex()
        [mu_m2,mu_l2,mu_u2,la_m2,la_lm2,la_um2,la_l2,la_u2,logN0_m2,logN0_lm2,
         logN0_um2,logN0_ll2,logN0_ul2,logN0_l2,logN0_u2] = self.PRS2.Vertex()
        [mu_m3,mu_l3,mu_u3,la_m3,la_lm3,la_um3,la_l3,la_u3,logN0_m3,logN0_lm3,
         logN0_um3,logN0_ll3,logN0_ul3,logN0_l3,logN0_u3] = self.PRS3.Vertex()
        [mu_m4,mu_l4,mu_u4,la_m4,la_lm4,la_um4,la_l4,la_u4,logN0_m4,logN0_lm4,
         logN0_um4,logN0_ll4,logN0_ul4,logN0_l4,logN0_u4] = self.PRS4.Vertex()
        [mu_m5,mu_l5,mu_u5,la_m5,la_lm5,la_um5,la_l5,la_u5,logN0_m5,logN0_lm5,
         logN0_um5,logN0_ll5,logN0_ul5,logN0_l5,logN0_u5] = self.PRS5.Vertex()
        [mu_m6,mu_l6,mu_u6,la_m6,la_lm6,la_um6,la_l6,la_u6,logN0_m6,logN0_lm6,
         logN0_um6,logN0_ll6,logN0_ul6,logN0_l6,logN0_u6] = self.PRS6.Vertex()
        data = {"Category":[self.lgdx[0],self.lgdx[1],self.lgdx[2]],
                "PRS Vertex (down)":[r'(log$_{10} N_0$, $\mu$, $\lambda$)',
                                     r'(log$_{10} N_0$ ,$\mu$, $\lambda$)',
                                     r'(log$_{10} N_0$, $\mu$, $\lambda$)'],
                "Most Likely, "+self.catx[0]:[(float(np.round(logN0_m1,2)),float(np.round(mu_m1,2)),float(np.round(la_m1,2))),
                                              (float(np.round(logN0_m2,2)),float(np.round(mu_m2,2)),float(np.round(la_m2,2))),
                                              (float(np.round(logN0_m3,2)),float(np.round(mu_m3,2)),float(np.round(la_m3,2)))],
                "Lighter "+self.catx[0]:[(float(np.round(logN0_l1,2)),float(np.round(mu_m1,2)),float(np.round(la_m1,2))),
                                         (float(np.round(logN0_l2,2)),float(np.round(mu_m2,2)),float(np.round(la_m2,2))),
                                         (float(np.round(logN0_l3,2)),float(np.round(mu_m3,2)),float(np.round(la_m3,2)))],
                "Heavier "+self.catx[0]:[(float(np.round(logN0_u1,2)),float(np.round(mu_m1,2)),float(np.round(la_m1,2))),
                                         (float(np.round(logN0_u2,2)),float(np.round(mu_m2,2)),float(np.round(la_m2,2))),
                                         (float(np.round(logN0_u3,2)),float(np.round(mu_m3,2)),float(np.round(la_m3,2)))],
                "Broader "+self.catx[0]+" PSD":[(float(np.round(logN0_lm1,2)),float(np.round(mu_l1,2)),float(np.round(la_lm1,2))),
                                                (float(np.round(logN0_lm2,2)),float(np.round(mu_l2,2)),float(np.round(la_lm2,2))),
                                                (float(np.round(logN0_lm3,2)),float(np.round(mu_l3,2)),float(np.round(la_lm3,2)))],
                "Narrower "+self.catx[0]+" PSD":[(float(np.round(logN0_um1,2)),float(np.round(mu_u1,2)),float(np.round(la_um1,2))),
                                                 (float(np.round(logN0_um2,2)),float(np.round(mu_u2,2)),float(np.round(la_um2,2))),
                                                 (float(np.round(logN0_um3,2)),float(np.round(mu_u3,2)),float(np.round(la_um3,2)))],
                "Larger "+self.catx[0]+" MMD":[(float(np.round(logN0_ll1,2)),float(np.round(mu_m1,2)),float(np.round(la_l1,2))),
                                               (float(np.round(logN0_ll2,2)),float(np.round(mu_m2,2)),float(np.round(la_l2,2))),
                                               (float(np.round(logN0_ll3,2)),float(np.round(mu_m3,2)),float(np.round(la_l3,2)))],
                "Smaller "+self.catx[0]+" MMD":[(float(np.round(logN0_ul1,2)),float(np.round(mu_m1,2)),float(np.round(la_u1,2))),
                                                (float(np.round(logN0_ul2,2)),float(np.round(mu_m2,2)),float(np.round(la_u2,2))),
                                                (float(np.round(logN0_ul3,2)),float(np.round(mu_m3,2)),float(np.round(la_u3,2)))],
                "Most Likely, "+self.catx[1]:[(float(np.round(logN0_m4,2)),float(np.round(mu_m4,2)),float(np.round(la_m4,2))),
                                              (float(np.round(logN0_m5,2)),float(np.round(mu_m5,2)),float(np.round(la_m5,2))),
                                              (float(np.round(logN0_m6,2)),float(np.round(mu_m6,2)),float(np.round(la_m6,2)))],
                "Lighter "+self.catx[1]:[(float(np.round(logN0_l4,2)),float(np.round(mu_m4,2)),float(np.round(la_m4,2))),
                                         (float(np.round(logN0_l5,2)),float(np.round(mu_m5,2)),float(np.round(la_m5,2))),
                                         (float(np.round(logN0_l6,2)),float(np.round(mu_m6,2)),float(np.round(la_m6,2)))],
                "Heavier "+self.catx[1]:[(float(np.round(logN0_u4,2)),float(np.round(mu_m4,2)),float(np.round(la_m4,2))),
                                         (float(np.round(logN0_u5,2)),float(np.round(mu_m5,2)),float(np.round(la_m5,2))),
                                         (float(np.round(logN0_u6,2)),float(np.round(mu_m6,2)),float(np.round(la_m6,2)))],
                "Broader "+self.catx[1]+" PSD":[(float(np.round(logN0_lm4,2)),float(np.round(mu_l4,2)),float(np.round(la_lm4,2))),
                                                (float(np.round(logN0_lm5,2)),float(np.round(mu_l5,2)),float(np.round(la_lm5,2))),
                                                (float(np.round(logN0_lm6,2)),float(np.round(mu_l6,2)),float(np.round(la_lm6,2)))],
                "Narrower "+self.catx[1]+" PSD":[(float(np.round(logN0_um4,2)),float(np.round(mu_u4,2)),float(np.round(la_um4,2))),
                                                 (float(np.round(logN0_um5,2)),float(np.round(mu_u5,2)),float(np.round(la_um5,2))),
                                                 (float(np.round(logN0_um6,2)),float(np.round(mu_u6,2)),float(np.round(la_um6,2)))],
                "Larger "+self.catx[1]+" MMD":[(float(np.round(logN0_ll4,2)),float(np.round(mu_m4,2)),float(np.round(la_l4,2))),
                                               (float(np.round(logN0_ll5,2)),float(np.round(mu_m5,2)),float(np.round(la_l5,2))),
                                               (float(np.round(logN0_ll6,2)),float(np.round(mu_m6,2)),float(np.round(la_l6,2)))],
                "Smaller "+self.catx[1]+" MMD":[(float(np.round(logN0_ul4,2)),float(np.round(mu_m4,2)),float(np.round(la_u4,2))),
                                                (float(np.round(logN0_ul5,2)),float(np.round(mu_m5,2)),float(np.round(la_u5,2))),
                                                (float(np.round(logN0_ul6,2)),float(np.round(mu_m6,2)),float(np.round(la_u6,2)))]}
        df = pd.DataFrame(data)
        ax.axis('off')
        colors = np.zeros((16,3),dtype='U7')
        colors[0,:] = '#ffffff'
        colors[1,:] = '#cccccc'
        colors[2,:] = '#ffffff'
        colors[3:5,:] = '#ffffcc'
        colors[5:7,:] = '#ccffff'
        colors[7:9,:] = '#ffccff'
        colors[9,:] = '#ffffff'
        colors[10:12,:] = '#ffffcc'
        colors[12:14,:] = '#ccffff'
        colors[14:16,:] = '#ffccff'
        colors2 = np.zeros(16,dtype='U7')
        colors2[0] = '#ffffff'
        colors2[1] = '#cccccc'
        colors2[2] = '#ffffff'
        colors2[3:5] = '#ffffcc'
        colors2[5:7] = '#ccffff'
        colors2[7:9] = '#ffccff'
        colors2[9] = '#ffffff'
        colors2[10:12] = '#ffffcc'
        colors2[12:14] = '#ccffff'
        colors2[14:16] = '#ffccff'
        table = ax.table(cellText=df.T.values,cellColours=colors,rowColours=colors2,rowLabels=df.columns,loc='center')
        table_props = table.properties()
        table_cells = table_props['children']
        table._autoColumns = []
        for cell in table_cells:
            cell.set_width(0.30)
            cell.set_height(0.06)
            cell.PAD = 0.03
        a_0 = [self.PRS1.a[0],self.PRS2.a[0],self.PRS3.a[0],self.PRS4.a[0],self.PRS5.a[0],self.PRS6.a[0]]
        b_0 = [self.PRS1.b[0],self.PRS2.b[0],self.PRS3.b[0],self.PRS4.b[0],self.PRS5.b[0],self.PRS6.b[0]]
        b_1 = [self.PRS1.b[1],self.PRS2.b[1],self.PRS3.b[1],self.PRS4.b[1],self.PRS5.b[1],self.PRS6.b[1]]
        with open(self.dirr+'VertexParams'+self.name+'.txt','w') as f:
            print(json.dumps('z vs. y (when positive, MMD decreases as mu increases)'),file=f)
            print(json.dumps(a_0),file=f)
            print(json.dumps('x vs. z (when positive, IWC decreases as MMD increases)'),file=f)
            print(json.dumps(b_0),file=f)
            print(json.dumps('x vs. y (when positive, IWC increases as mu increases)'),file=f)
            print(json.dumps(b_1),file=f)

    def VolCrossSix(self,ax,xmax,ymax,unit=""):
        """
        Plots six PRS cross-sections in one figure.
        
        Args:
            ax: Plot axes.
            xmax: Upper limit for x axis (mu).
            ymax: Upper limit for y axis (lambda [mm^-1]).
            unit: Unit for figure title. The default is "".
        """
        var = self.PRS1.Plot(ax,self.c(0))
        x1 = var[0]
        y1 = var[1]
        var = self.PRS2.Plot(ax,self.c(0.4))
        x2 = var[0]
        y2 = var[1]
        var = self.PRS3.Plot(ax,self.c(0.8))
        x3 = var[0]
        y3 = var[1]
        var = self.PRS4.Plot(ax,self.c(0),True)
        x4 = var[0]
        y4 = var[1]
        var = self.PRS5.Plot(ax,self.c(0.4),True)
        x5 = var[0]
        y5 = var[1]
        var = self.PRS6.Plot(ax,self.c(0.8),True)
        x6 = var[0]
        y6 = var[1]
        ax.scatter(x1,y1,25,color=self.c(0),zorder=2.5,label=self.lgdx[0])
        ax.scatter(x2,y2,25,color=self.c(0.4),zorder=2.5,label=self.lgdx[1])
        ax.scatter(x3,y3,25,color=self.c(0.8),zorder=2.5,label=self.lgdx[2])
        ax.scatter(x4,y4,25,color=self.c(0),zorder=2.5,marker='^')
        ax.scatter(x5,y5,25,color=self.c(0.4),zorder=2.5,marker='^')
        ax.scatter(x6,y6,25,color=self.c(0.8),zorder=2.5,marker='^')
        ax.set_xlabel(r"$\mu$")
        ax.set_ylabel(r"$\lambda$ [mm$^{-1}$]")
        ax.set_xlim([-1,xmax])
        ax.set_ylim([0,ymax])
        ax.legend(loc='upper center',bbox_to_anchor=(0.5,1),ncol=3,fontsize=12)
        ax.set_title("Cross Sections for "+self.name+unit)