import numpy as np
from collections import Counter
from Data.load import load_data, split_data

# Step 1: Load and split the data
lInf, lPur, lPar = load_data()
lInf_train, lInf_eval = split_data(lInf, 4)
lPur_train, lPur_eval = split_data(lPur, 4)
lPar_train, lPar_eval = split_data(lPar, 4)

# Step 2: Build dictionary from training data
def build_dictionary(lists):
    # Combine all training lists
    all_text = ""
    for sublist in lists:
        for tercet in sublist:
            all_text += tercet + " "
    all_text = all_text.strip()
    # Simple tokenization (you may want to refine this)
    words = all_text.lower().split()
    return set(words)

dictionary = build_dictionary([lInf_train, lPur_train, lPar_train])

# Step 3: Function to get word counts for a tercet using the training dictionary
def get_word_counts(tercet, dictionary):
    tokens = tercet.lower().split()
    # Keep only words in the dictionary
    filtered_tokens = []
    for word in tokens:
        if word in dictionary:
            filtered_tokens.append(word)
    tokens = filtered_tokens
    return Counter(tokens)

# Step 4: Count word occurrences per Cantica (training data)
def count_words(tercets, dictionary):
    count = Counter()
    for tercet in tercets:
        count.update(get_word_counts(tercet, dictionary))
    return count

N_inf = count_words(lInf_train, dictionary)
N_pur = count_words(lPur_train, dictionary)
N_par = count_words(lPar_train, dictionary)

# Step 5: Compute ML estimates (relative frequencies) for each class
def compute_probabilities(word_count):
    total = sum(word_count.values())
    # Avoid division by zero
    probabilities = {}
    for word, count in word_count.items():
        probabilities[word] = count / total
    return probabilities

pi_inf = compute_probabilities(N_inf)
pi_pur = compute_probabilities(N_pur)
pi_par = compute_probabilities(N_par)

# Step 6: Classify a new tercet (example)
def classify_tercet(tercet, dictionary, class_models):
    # class_models is a dict with class names as keys and their estimated probabilities as values
    word_counts = get_word_counts(tercet, dictionary)
    log_likelihoods = {}
    for class_name, pi in class_models.items():
        # Initialize log likelihood
        log_likelihood = 0.0
        for word, count in word_counts.items():
            if word in pi and pi[word] > 0:
                log_likelihood += count * np.log(pi[word])
            # Words with zero probability (unseen in training) can be handled by smoothing
        log_likelihoods[class_name] = log_likelihood
    # Return the class with the highest log likelihood
    return max(log_likelihoods, key = log_likelihoods.get), log_likelihoods

class_models = {
    'Inferno': pi_inf,
    'Purgatorio': pi_pur,
    'Paradiso': pi_par
}

# Example: classify the first tercet in the evaluation set for Inferno
predicted_class, ll = classify_tercet(lInf_eval[0], dictionary, class_models)
print("Predicted class:", predicted_class)
print("Log-likelihoods:", ll)
