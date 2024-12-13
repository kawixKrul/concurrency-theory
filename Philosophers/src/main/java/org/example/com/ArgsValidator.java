package org.example.com;
public class ArgsValidator {
    public static int validateProblemSizeArg(String arg) {
        var x = arg.split("=");
        if (x[0].equals("-s")) {
            return Integer.parseInt(x[1]);
        }
        else {
            throw new IllegalArgumentException("Bad size argument");
        }
    }

    public static int validateSimulationTimeArg(String arg) {
        var x = arg.split("=");
        if (x[0].equals("-t")) {
            return Integer.parseInt(x[1]);
        }
        else {
            throw new IllegalArgumentException("Bad simulation time argument");
        }
    }

    public static int validateProblemTypeArg(String arg) {
        var x = arg.split("=");
        if (x[0].equals("-f")) {
            return Integer.parseInt(x[1]);
        }
        else {
            throw new IllegalArgumentException("Bad philsopher type argument");
        }
    }
}
