# Penn State AI801 Team9 BlackJack Project
## Scripts:
### Interactive Script:
#### Rainman_Interactive
##### About
This script allows users to play Blackjack on their own and maintain a reward system to see how they would do as the AI.
##### How To Play
1. download the repository
2. Open the Rainman_Interactive.py script
3. Enter your initial bet (1, 2, 5, or 10)
4. After reviewing your initial hand, choose if you would like to hit or stay
  a. If the drawn card is an ace, choose if you would like to convert to a 1 or leave as 11
5. If the value is still under 21 after hitting, choose again (and so on)
6. After the game has concluded, you will be given the option to continue playing or end.
7. After ending the game, a summary will be provided
### AI-Env Script
#### Rainman_WithAgent
##### About
This script was set up as an OpenGym Environment and runs using a discrete space approach for each of the actions:
- hit/stay (discrete space of 2)
- bet (discrete space of 4)
- convert ace (discrete space of 2)
- continue playing (discrete space of 2)
### Pre-Defined Scripts
#### Rainman_AlwaysHit
##### About

#### Rainman_AlwaysStay
##### About

#### Rainman_Conditional
##### About

#### Rainman_BankOptimizationConditional
##### About

#### Rainman_AllowNegativeConditional
##### About

#### Rainman_Randomized
##### About
