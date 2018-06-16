#!/usr/bin/env python

import argparse
import sys
import os
import yaml
import zipfile

def db4pkg():
    db_source = """
    ZLIB:
        path: builtins/zlib/
    Graf3d:
        deps: Graf Hist Gpad MathCore
        path: graf3d/g3d/
    Graf:
        deps: Hist Matrix MathCore
        path: graf2d/graf/
    Gpad:
        deps: Graf Hist
        path: graf2d/gpad/
    Hist:
        deps: MathCore Matrix
        path: hist/hist/
    Hbook:
        deps: Hist Matrix Tree Graf TreePlayer
        path: hist/hbook/
    ROOTHistDraw:
        deps: ROOTGraphicsPrimitives
        path: hist/histdraw/
    HistPainter:
        deps: Graf Hist Matrix MathCore ROOTHistDraw
        path: hist/histpainter/
    Spectrum:
        deps: Hist Matrix
        path: hist/spectrum/
    SpectrumPainter:
        deps: Graf Hist
        path: hist/spectrumpainter/
    Unfold:
        deps: Hist XMLParser Matrix
        path: hist/unfold/
    Tree:
        deps: Net MathCore
        path: tree/tree/
    ROOTDataFrame:
        deps: Tree TreePlayer Hist ROOTVecOps
        path: tree/dataframe/
    TreePlayer:
        deps: Tree Graf3d Graf Hist Gpad MathCore
        path: tree/treeplayer/
    XMLIO:
        path: io/xml/
    Net:
        path: net/net/
    XMLParser:
        path: io/xmlparser/
    SQLIO:
        deps: Net
        path: io/sql/
    RFIO:
        deps: Net
        path: io/rfio/
    HDFS:
        deps: Net
        path: io/hdfs/
    GFAL:
        deps: Net
        path: io/gfal/
    DCache:
        deps: Net
        path: io/dcache/
    RCastor:
        deps: Net
        path: io/castor/
    MathCore:
        path: math/mathcore/
    Matrix:
        deps: MathCore
        path: math/matrix/
    Quadp:
        deps: Matrix
        path: math/quadp/
    FFTW:
        deps: MathCore
        path: math/fftw/
    Fumili:
        deps: MathCore Hist Graf
        path: math/fumili/
    Foam:
        deps: MathCore Hist
        path: math/foam/
    Genetic:
        deps: MathCore TMVA
        path: math/genetic/
    GenVector:
        deps: MathCore Physics
        path: math/genvector/
    MathMore:
        deps: MathCore
        path: math/mathmore/
    Minuit:
        deps: Graf Hist Matrix MathCore
        path: math/minuit/
    Minuit2:
        deps: MathCore Hist
        path: math/minuit2/
    MLP:
        deps: Hist Matrix Tree Graf Gpad TreePlayer MathCore
        path: math/mlp/
    Physics:
        deps: Matrix MathCore
        path: math/physics/
    Rtools:
        deps: MathCore RInterface
        path: math/rtools/
    Smatrix:
        deps: Matrix MathCore
        path: math/smatrix/
    Splot:
        deps: Matrix Hist Tree TreePlayer Graf3d Graf MathCore
        path: math/splot/
    Unuran:
        deps: Hist MathCore
        path: math/unuran/
    ROOTVecOps:
        deps: Matrix
        path: math/vecops/
    """
    db_manifest = yaml.load(db_source)
    return db_manifest
