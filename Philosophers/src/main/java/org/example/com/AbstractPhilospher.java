package org.example.com;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.concurrent.atomic.AtomicInteger;

public abstract class AbstractPhilospher extends Thread {
    static final AtomicInteger idGenerator = new AtomicInteger(0);
    private static final int waitingTime = 10;
    protected final int id;
    protected final Fork left;
    protected final Fork right;
    private long startedThinkingAt = System.currentTimeMillis();
    private final BufferedWriter writer;

    public AbstractPhilospher(Fork left, Fork right) throws IOException {
        this.left = left;
        this.right = right;
        this.id = idGenerator.getAndIncrement();
        this.writer = new BufferedWriter(new FileWriter("philospher"+id+".csv"));
        writer.write("id,time\n");
        writer.flush();
    }

    protected void think() throws InterruptedException {
        startedThinkingAt = System.currentTimeMillis();
        System.out.println("Filozof " + id + " : kontempluje");
        Thread.sleep((int) (Math.random() * waitingTime));
    }

    protected void eat() throws InterruptedException, IOException {
        System.out.println("Filozof "+id +" : mniam, mniam");
        logToFile();
        Thread.sleep((int) (Math.random() * waitingTime));
    }

    private void logToFile() throws IOException {
        long timeElapsed = System.currentTimeMillis() - startedThinkingAt;
        writer.write(id+","+timeElapsed+"\n");
        writer.flush();
    }
    public void lastLog() throws IOException {
        logToFile();
        writer.close();
    }

    @Override
    public void interrupt() {
        super.interrupt();
        try {
            logToFile();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
