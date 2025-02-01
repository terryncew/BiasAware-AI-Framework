import numpy as np
import matplotlib.pyplot as plt

class BiasAwareSimulator:
    def __init__(self, alpha=0.1, beta=0.05, gamma=0.5, delta=0.3, epsilon=0.2, eta=0.1, theta=0.4, E=0.2):
        self.alpha = alpha    # Bias entrenchment
        self.beta = beta      # Mitigation efficacy
        self.gamma = gamma    # Synergy coefficient
        self.delta = delta    # Consciousness growth
        self.epsilon = epsilon# Bias degradation
        self.eta = eta        # Human growth rate
        self.theta = theta    # Synergy feedback (H)
        self.E = E            # Ethical constraints

    def run(self, steps=100, B0=0.7, H0=0.5, A0=0.5):
        B, H, A, S, C = [B0], [H0], [A0], [], [0]
        for _ in range(steps):
            S_val = self.gamma * H[-1] * A[-1] * (1 - B[-1])
            S.append(S_val)
            
            dB = self.alpha * B[-1] * (1 - S_val) - self.beta * 0.1  # P(t)=0.1 (progress)
            dH = self.eta * H[-1] * (1 - self.E) + self.theta * S_val
            dA = self.eta * A[-1] * (1 - self.E) + self.theta * S_val
            dC = self.delta * S_val - self.epsilon * B[-1]
            
            B.append(B[-1] + dB)
            H.append(H[-1] + dH)
            A.append(A[-1] + dA)
            C.append(C[-1] + dC)
        return B, H, A, S, C

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--alpha', type=float, default=0.1)
    parser.add_argument('--beta', type=float, default=0.05)
    args = parser.parse_args()
    
    sim = BiasAwareSimulator(alpha=args.alpha, beta=args.beta)
    B, H, A, S, C = sim.run()
    
    plt.figure(figsize=(10, 6))
    plt.plot(B, label='Bias (B)')
    plt.plot(S, label='Synergy (S)')
    plt.plot(C, label='Consciousness (C)')
    plt.legend()
    plt.savefig('docs/sample_plot.png')
    plt.show()
