from gen_alg import gen_alg


def takeSecond(elem):
    return elem[1]


def testing():
    results12=[]
    # for _ in range(30):
    #     results.append(gen_alg('berlin52'))
    chance_to_pmx_range=[x/100 for x in range(80,96,5)]
    chance_to_mutate_range=[x/100 for x in range(4,19,2)]
    k_participants_range=[2,3,4]
    tournament_pop_range=[x for x in range(800,1001,100)]
    max_generation_range=[x for x in range(1000,5001,1000)]

    for chance_to_mutate in chance_to_mutate_range:
        for chance_to_pmx in chance_to_pmx_range:
            for k_participants in k_participants_range:
                for tournament_pop in tournament_pop_range:
                    for max_generation in max_generation_range:
                        result11=gen_alg('berlin52', base_pop=200,
                                                    max_generation=max_generation,
                                                    tournament_pop=tournament_pop,
                                                    k_participants=k_participants,
                                                    chance_to_pmx=chance_to_pmx,
                                                    chance_to_mutate=chance_to_mutate)                           
                        results12.append(result11)

                    
    results12.sort(key=takeSecond)

    print(f'\n############## Final Results ############\n')
    for x in results12:
        print("-".join(map(str,x[0])), x[1])

    print(f'\n############## Top Result   ############\n')
    print([print(x) for x in results12[0]])
    print("-".join(map(str,results12[0][0])), results12[0][1])

    with open('results/result{}.txt'.format(), 'w+') as f:
        f.writelines(str(results12))