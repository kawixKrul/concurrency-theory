package org.example.com;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.function.BiFunction;

public class PhilosopherProblemFactory {
    public static List<AbstractPhilospher> createPhilosophersForProblemType(
            int problemSize,
            int problemType) {

            BiFunction<Fork, Fork, ? extends AbstractPhilospher> philosopherConstructor = switch (problemType) {
                case 1 -> (left, right ) -> { try
                    {
                        return new PhilospherNaive(left, right);
                    } catch (IOException ignored) {}
                    throw  new RuntimeException("");
                };
                case 2 -> (left, right ) -> { try
                {
                    return new PhilospherStravation(left, right);
                } catch (IOException ignored) {}
                    throw  new RuntimeException("");
                };
                case 3 -> (left, right ) -> { try
                {
                    return new PhilospherAsymetric(left, right);
                } catch (IOException ignored) {}
                    throw  new RuntimeException("");
                };
                case 4 -> (left, right ) -> { try
                {
                    return new PhilospherStochastic(left, right);
                } catch (IOException ignored) {}
                    throw new RuntimeException("");
                };
                case 5 -> {
                    PhilospherArbiter.createArbiter(problemSize);
                    yield (left, right ) -> { try
                    {
                        return new PhilospherArbiter(left, right);
                    } catch (IOException ignored) {}
                        throw  new RuntimeException("");
                    };
                }
                case 6 -> {
                    PhilospherDining.createDiningRoom(problemSize);
                    yield (left, right ) -> { try
                    {
                        return new PhilospherDining(left, right);
                    } catch (IOException ignored) {}
                        throw  new RuntimeException("");
                    };
                }
                default -> throw new IllegalArgumentException("Problem type not supported");
            };
        List<Fork> forks = new ArrayList<>(problemSize);
        for (int i = 0; i < problemSize; i++) {
            forks.add(new Fork());
        }

        List<AbstractPhilospher> philosophers = new ArrayList<>(problemSize);
        for (int i = 0; i < problemSize; i++) {
            Fork leftFork = forks.get(i);
            Fork rightFork = forks.get((i + 1) % problemSize);
            philosophers.add(philosopherConstructor.apply(leftFork, rightFork));
        }

        return philosophers;
    }
}
