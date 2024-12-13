package org.example.com;

import java.io.IOException;
import java.util.concurrent.Semaphore;

public class PhilospherDining extends AbstractPhilospher{
    private static Semaphore diningRoom;
    public PhilospherDining(Fork left, Fork right) throws IOException {
        super(left, right);
    }

    public static void createDiningRoom(int problemSize) {
        PhilospherDining.diningRoom = new Semaphore(problemSize-1);
    }

    @Override
    public void run() {
        try {
            while (!Thread.interrupted()){
                think();
                if (diningRoom.tryAcquire()) {
                    left.getFork();
                    right.getFork();
                    eat();
                    left.putFork();
                    right.putFork();
                    diningRoom.release();
                } else {
                    right.getFork();
                    left.getFork();
                    eat();
                    left.putFork();
                    right.putFork();
                }}
        } catch (InterruptedException | IOException e) {
            Thread.currentThread().interrupt();
        }
    }
}
