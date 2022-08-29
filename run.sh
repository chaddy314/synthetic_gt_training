#!/usr/bin/env bash
#SBATCH --job-name=synthetic_gt_training
#SBATCH --output=synthetic_gt_training.log

# get environments from json

SYNTH_GT_ENV=$(python3 json_helper.py $1 synthgt-env)
CALALAMARI_GT_ENV=$(python3 json_helper.py $1 calamari-env)
SKIP_SYNTH_GEN=$(python3 json_helper.py $1 skip-synth-gen)
SKIP_TRAINING=$(python3 json_helper.py $1 skip-training)
SKIP_EVALUATION=$(python3 json_helper.py $1 skip-evaluation)
echo "${SYNTH_GT_ENV}"
echo "${CALALAMARI_GT_ENV}"

if [ $SKIP_SYNTH_GEN = "False" ]; then
    source "${SYNTH_GT_ENV}"
    python3 synth_gt_helper.py $1
    deactivate
else
    echo "Skipping Synthetic Text Generation"
fi

if [ $SKIP_TRAINING = "False" ]; then
    source "${CALALAMARI_GT_ENV}"
    python3 calamari_helper.py $1
else
    echo "Skipping Training"
fi

if [ $SKIP_EVALUATION = "False" ]; then
    EVAL_DIR=$(python3 json_helper.py $1 eval-dir evaluator)
    OUTPUT_DIR=$(python3 json_helper.py $1 xlsx-output evaluator)
    python3 evaluate_over_models.py  $1
else
    echo "Skipping Training" "${EVAL_DIR}" "${OUTPUTDIR_DIR}"
fi
deactivate
