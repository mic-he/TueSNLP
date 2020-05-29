#!/usr/bin/env python3
""" Template for Assignment 2
    See <https://snlp2019.github.io/a2/> for instructions.

    Please make sure that the command line interface works as
    defined below in your final submission. Part of your grade will be
    based on correct functioning of this interface. You can make
    additions, or change it during development process,
    However, unexpected output (e.g., extra lines of output in
    'predict' argument below) will result in 0 points (out fo 2)
    for performance.
"""

import argparse
from sklearn.metrics import precision_recall_fscore_support

def encode(filename):
    """ Read the indicated file name, return the labels (language
    families) and one-hot encoded feature vectors.
    You can modify the interface of this function (you may
    need to modify it for exercises 3 & 4).
    """
    pass

def classify(filename):
    """ Read and encode the file using encode(),
    train a logistic regression classifier on the 2/3rd of
    the data, test it on the remaining 1/3rd.
    The function should not return any value but output the
    macro-averaged precision recall and f-score on the training and test sets.
    """
    pass


def tune(filename):
    """ Read and encode the file using encode(),
    tune a classifier with any method you chose
    and return the best hyperparameter values as a dictionary.
    For example, if you used logistic regression,
    and tuned only for the regularization parameter 'C'
    your output may look like {'C': 1.0}.
    """
    pass

def predict(trainfile, testfile, parameters=None):
    """ Return predictions for testfile after training the 
    model on the trainfile with the given parameters.
    If the parameters are not given,
    they should default to the values you determined during exercise 2.3.
    """
    pass
    

if __name__ == '__main__':
    argp = argparse.ArgumentParser()
    argp.add_argument('command',
            choices=('classify', 'tune', 'predict', 'score'))
    argp.add_argument('train', help="Training file name")
    argp.add_argument('--test', help="Test file name")
    argp.add_argument('--goldstd', help="Gold standard labels")
    args = argp.parse_args()

    if args.command == 'classify':
        classify(args.train)
    elif args.command == 'tune':
        print(tune(args.train))
    elif args.command in {'predict', 'score'}:
        if not args.test:
            args.test = args.train
        predictions = predict(args.train, args.test)
        if args.command == 'predict':
            for pred in predictions:
                print(pred)
        if args.command == 'score':
            if args.goldstd:
                with open(args.goldstd) as fp:
                    gold_labels = fp.readlines().split()
            else:
                gold_labels, _ = encode(args.test)
            p, r, f, s = precision_recall_fscore_support(
                            gold_labels, predictions, average='macro')
            print(f)
