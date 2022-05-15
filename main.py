from functions.genetic_algorithm import genetic_algorithm
if __name__ == "__main__":

    result=genetic_algorithm( file_name='berlin52',
                        base_pop=100,
                        max_generation=50000,
                        tournament_pop=60,
                        k_participants=2,
                        dhm_ilc=False,
                        crossover_chance=0.97,
                        mutation_chance=0.05,
                        tracking=1000,
                        exploitation_start=0.3,
                        show_results=True,
                        save_results=False,
                        plot_results=True)