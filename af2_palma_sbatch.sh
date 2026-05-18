#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks 4
#SBATCH --cpus-per-task 1
#SBATCH --mem=20G
#SBATCH --partition=gpu2080
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --job-name=idp_2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=username@uni-muenster.de

module --force purge

ml palma/2021a
ml GCC/10.3.0
ml OpenMPI/4.1.1
ml AlphaFold/2.1.1-CUDA-11.3.1
wait
export ALPHAFOLD_DATA_DIR=/Applic.HPC/data/alphafold

cd path/to/fasta

alphafold \
    --fasta_paths=/scratch/tmp/username/path/fasta/XYZ.fasta \
    --model_preset=monomer \
    --output_dir=/scratch/tmp/username/path/results/ \
    --max_template_date=2022-12-19 \
    --is_prokaryote_list=false \
    --db_preset=reduced_dbs \
    --data_dir=/Applic.HPC/data/alphafold \

#ENV
