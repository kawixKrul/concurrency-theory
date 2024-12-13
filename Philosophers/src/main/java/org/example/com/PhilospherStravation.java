package org.example.com;

import java.io.IOException;

public class PhilospherStravation extends AbstractPhilospher{

    public PhilospherStravation(Fork left, Fork right) throws IOException {
        super(left, right);

    }

    @Override
    public void run() {
        try {
            while (!Thread.interrupted()){
                think();
                while (left.getIsTaken() || right.getIsTaken()) {
                    wait();
                }
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
