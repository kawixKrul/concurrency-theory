package org.example.com;

import java.io.IOException;

public class PhilospherStochastic extends AbstractPhilospher {
    public PhilospherStochastic(Fork left, Fork right) throws IOException {
        super(left, right);
    }

    @Override
    public void run() {
        try {
            while (!Thread.interrupted()) {
                think();
                if (Math.random() > 0.5) {
                    right.getFork();
                    left.getFork();
                } else {
                    left.getFork();
                    right.getFork();
                }
                eat();
                left.putFork();
                right.putFork();
            }
        } catch (InterruptedException | IOException e) {
            Thread.currentThread().interrupt();
        }
    }
}
