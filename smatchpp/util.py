import numpy as np
import logging
import time
import os

logger = logging.getLogger("__main__")


def read_reify_table(p="/resource/reify_table.txt", lower=False):
    """load reification rules"""
    
    path = os.path.dirname(__file__)

    with open(path + p, "r") as f:
        lines = [l for l in f.read().split("\n") if l]

    rel_rule = {}
    rel_rule_inverse = {}

    for line in lines:
        if lower:
            line = line.lower()
        spl = line.split("|")
        spl = [x.strip() for x in spl]

        rel_rule[spl[0]] = [spl[1], spl[2], spl[3]]
        rel_rule_inverse[spl[1]] = [spl[0], spl[2], spl[3]]

    return rel_rule, rel_rule_inverse

def xor(a, b):
    if a and b:
        return False
    if a or b:
        return True
    return False


def get_var_concept_dict(triples):
    """get mapping from variables to concepts """
    vc = {}
    for tr in triples:
        if tr[1] == ":instance":
            vc[tr[0]] = tr[2]
    vc["root"] = "root"
    return vc


def isroot(var, triples):
    """ check if triple is root """
    trs = [tr for tr in triples if tr[2] == var]
    if not trs:
        return False
    for tr in trs:
        if tr[1] == ":root":
            return True
    return False

def add_dict(todic, fromdic):
    for key in fromdic:
        if key not in todic:
            todic[key] = fromdic[key]
        else:
            todic[key] += fromdic[key]
    return None

def append_dict(todic, fromdic):
    for key in fromdic:
        if key not in todic:
            todic[key] = [fromdic[key]]
        else:
            todic[key].append(fromdic[key])
    return None


def score(alignmat, unarymatch_dict, binarymatch_dict):
    """Score an alignment candidate

        Args:
            alignmat (2d array): alignments from V to V'
            unarymatch_dict (dict): scores of unary alignments
            binarymatch_dict (dict): scores of binary alignments

        Returns:
            score (float)
    """

    # init
    sc = 0.0
    V = range(alignmat.shape[0])

    # iterate over nodes in V
    for i in V:
        # get an alignment i -> j
        j = alignmat[i]
        #add unary triple matches
        sc += unarymatch_dict[(i, j)]
        # iterate over more nodes in V
        for k in V:
            # alignment now i-> j AND k -> l
            l = alignmat[k]
            # add score for binary triple matches
            sc += binarymatch_dict[(i, j, k, l)]
    return sc

def alignmat_compressed(alignmat):
    alignmatargmax = alignmat.argmax(axis=1)
    alignmatargmax[alignmat.sum(axis=1) == 0] = -1
    alignmat = alignmatargmax
    return alignmat

def alignmat_decompressed(alignmat):
    a = np.zeros((len(alignmat), len(alignmat)))
    for i, j in enumerate(alignmat):
        a[i, j] = 1    
    return a