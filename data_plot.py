   def plot_ky_freq(self,w=0.5,wmax=0.0,norm='elec',fig=None):
      if fig is None:
         fig = plt.figure(MYDIR,figsize=(self.lx,self.ly))
      self.getbigfield()
      theta = 0.0
      field = 0
      self.getnorm(norm) ; t = self.tnorm ; kx = self.kxnorm
      f,ft = self.kxky_select(theta,field,'phi',0)
      newf = np.log(f)
#      mode_weight = np.abs(f)
#      total_weight = sum(mode_weight)
      lent = len(t)-1
      im = 1j
      for i in range(1,lent):
          newf[:,:,i] = (np.log(f[:,:,i]/f[:,:,i-1]))/(t[i]-t[i-1])
      p = np.sum(newf[:,:,:],axis=1)*im
#      p = np.sum(newf[:,:,:]*mode_weight[:,:,:],axis=1)/total_weight
#      lasttime = np.shape(p)
#      last_t = lasttime[1]-1
      real_omega = p.real
      imaginary_gamma = p.imag
      #======================================
      # Omega
      ax = fig.add_subplot(121)
      ax.grid(which="both",ls=":")
      ax.grid(which="major",ls=":")
      ax.set_xlabel(self.kstrx)
      ax.set_ylabel(self.fstr[0])

      ax.plot(kx, real_omega[:,lent],color='blue')
      ax.plot(kx, real_omega[:,lent],"o",color='k')
#      plt.xlim([-15, 15])
#      if len(kx) > 1:
#         ax.set_xlim([0,kx[-1]])
      #======================================

      #======================================
      # Gamma
      ax = fig.add_subplot(122)
      ax.grid(which="both",ls=":")
      ax.grid(which="major",ls=":")
      ax.set_xlabel(self.kstrx)
      ax.set_ylabel(self.fstr[1])

      ax.plot(kx, imaginary_gamma[:,lent],color='red')
      ax.plot(kx, imaginary_gamma[:,lent],"o",color='k')
#      plt.xlim([-15, 15])
#      if len(kx) > 1:
#         ax.set_xlim([0,kx[-1]])
      #======================================
      fig.tight_layout(pad=0.3)
#      print(kx)
