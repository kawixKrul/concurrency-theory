package org.example.com;

public class Fork {
    private boolean isTaken = false;

    public synchronized void getFork() throws InterruptedException {
        while (isTaken) {
            wait();
        }
        isTaken = true;
    }

    public synchronized void putFork() {
        isTaken = false;
        notifyAll();
    }

    public synchronized boolean getIsTaken() {
        return this.isTaken;
    }
}
