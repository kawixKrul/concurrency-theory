package org.example.com;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    public static void main(String[] args) throws InterruptedException, IOException {
        System.out.println("Argi:" + args);
        int problemSize = 0;
        int simulationTime = 0;
        int philospherType = 0;
        try {
        problemSize = ArgsValidator.validateProblemSizeArg(args[0]);
        simulationTime = ArgsValidator.validateSimulationTimeArg(args[1]);
        philospherType = ArgsValidator.validateProblemTypeArg(args[2]);
        } catch (IllegalArgumentException e) {
            System.err.println("Error parsing arguments: " + e.getMessage());
            System.exit(1);
        }
        var execService = Executors.newFixedThreadPool(problemSize);

        var philsophers = PhilosopherProblemFactory.createPhilosophersForProblemType(problemSize, philospherType);
        for (Thread t : philsophers) {
            execService.submit(t);
        }

        Thread.sleep(simulationTime * 1000);
        execService.shutdownNow();

        for (var p : philsophers) {
            p.lastLog();
        }
        var csvs = IntStream.range(0,problemSize)
                .mapToObj(x->"philospher"+x+".csv")
                .toList();

        var outpath = "philospherProblem"+philospherType+".csv";

        try {
            mergeCSVFiles(csvs, outpath);
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    public static void mergeCSVFiles(List<String> csvs, String outputPath) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(outputPath))) {
            writer.write("id,time\n");
            for (var file : csvs) {
                try (BufferedReader reader = new BufferedReader(new FileReader(file))) {
                    String line;
                    reader.readLine();
                    while ((line = reader.readLine()) != null) {
                        writer.write(line + "\n");
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}