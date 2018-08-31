#!/usr/bin/env python3

# Any probabilities are 1 in n

BASE_YEAR = 1443
# change according to probability
PROFESSIONS = ["farmer"]*2 + ["merchant"]

GENDERS = ["male", "female"]
ATTRIBUTES = ["o", "c", "e", "a", "n", "p", "i"]
CAP_CUTOFF = 3.5
LIFE_EXPECTANCY = 40*4
# standard deviation for life expectancy random gaussian distribution
LIFE_EXPECTANCY_SD = 5*4

HARSH_WINTER_CHANCE = 5
HARSH_WINTER_MOD = 0.5

WORKING_CHILD_MIN_AGE = 8*4

ADULT_FOOD_NOURISHED = 10
ADULT_FOOD_HUNGRY = 7
ADULT_FOOD_MALNOURISHED = 4

CHILD_FOOD_NOURISHED = 6
CHILD_FOOD_HUNGRY = 4
CHILD_FOOD_MALNOURISHED = 2

ADULT_BASE_HARVEST = 50
CHILD_BASE_HARVEST = 25

MERCHANT_BASE_INCOME = 15

MAX_FOOD_STORAGE_PER_PERSON = 100

RAPPORT_DECAY = 0.05

SUICIDE_MIN_MOOD_LEVEL = -1.9

START_INTERACTION_MIN_AGE = 3*4
DT_CHANCE = 3
DT_RAPPORT_GAIN = 0.09
DT_MIN_AGE = 8*4
CHAT_RAPPORT_GAIN = 0.03
ARGUMENT_RAPPORT_GAIN = -0.05
ANGRY_LOOK_RAPPORT_GAIN = -0.03
CAP_MODIFIER = 4  # divided by
MIN_ASKOUT_AGE = 16*4

MIN_ARGUMENT_AGE = 5*4

# Modifier applied to rapport if someone else initiated
# the interaction.
INTERACTED_WITH_MOD = (2/3)
