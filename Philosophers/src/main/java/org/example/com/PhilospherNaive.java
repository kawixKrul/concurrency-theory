package org.example.com;

import java.io.IOException;

public class PhilospherNaive extends AbstractPhilospher{
    public PhilospherNaive(Fork left, Fork right) throws IOException {
        super(left, right);
    }

    @Override
    public void run() {
        try {
            while (!Thread.interrupted()){
                    think();
                    left.getFork();
                    right.getFork();
                    eat();
                    left.putFork();
                    right.putFork();
                }
        } catch (InterruptedException | IOException e) {
            Thread.currentThread().interrupt();
        }
    }
}
