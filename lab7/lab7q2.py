

def learn_prior(file_name, pseudo_count=0):

    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)] 
        
    print(training_examples)
        
prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))        