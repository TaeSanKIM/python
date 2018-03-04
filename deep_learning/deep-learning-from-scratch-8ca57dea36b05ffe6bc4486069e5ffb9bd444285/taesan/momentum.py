class momentum:
    def __init__(self, momentum = 0.9, Ir = 0.01):
        self.Ir = Ir
        self.momentum = momentum
        self.v = None

    def update(self, params, grads):
        if self.v == None:
            self.v={}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] = self.Ir * grads[key]
            parmas[key] -= self.v[key]
            
