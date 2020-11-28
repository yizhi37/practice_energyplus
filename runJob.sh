#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=6
#SBATCH --time=30:00
#SBATCH --partition=shas-testing
#SBATCH --output=sample-%j.out

module load python
module load R
ml
python runModel.py
