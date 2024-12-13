package org.example.com;

import java.io.IOException;

public class PhilospherAsymetric extends AbstractPhilospher{
    public PhilospherAsymetric(Fork left, Fork right) throws IOException {
        super(left, right);
    }

    @Override
    public void run() {
        try {
            while (!Thread.interrupted()) {
                think();
                if (id % 2 == 0) {
                    right.getFork();
                    left.getFork();
                } else {
                    left.getFork();
                    right.getFork();
                }
               eat();
                left.putFork();
                right.putFork();}
        } catch (InterruptedException | IOException e) {
            Thread.currentThread().interrupt();
        }
    }
}
