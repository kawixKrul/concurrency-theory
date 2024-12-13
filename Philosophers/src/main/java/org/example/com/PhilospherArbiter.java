package org.example.com;

import java.io.IOException;
import java.util.concurrent.Semaphore;

public class PhilospherArbiter extends AbstractPhilospher {
    private static Semaphore arbiter;
    public PhilospherArbiter(Fork left, Fork right) throws IOException {
        super(left, right);
    }

    public static void createArbiter(int problemSize) {
        PhilospherArbiter.arbiter = new Semaphore(problemSize-1);
    }

    @Override
    public void run() {
        try {
            while(!Thread.interrupted()) {
                arbiter.acquire();
                think();
                left.getFork();
                right.getFork();
                eat();
                left.putFork();
                right.putFork();
                arbiter.release();
            }
        } catch (InterruptedException | IOException e) {
            Thread.currentThread().interrupt();
        }
    }
}
