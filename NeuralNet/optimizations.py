class Optimizer:
    @staticmethod
    def grad_descent(weights, alpha, grad):
        desc_weights = map(lambda l_w, l_g: l_w - alpha * l_g, weights, grad)
        return desc_weights

    @staticmethod
    def stochastic_grad_descent(weights, batch_size, alpha, grad, ):
        pass
