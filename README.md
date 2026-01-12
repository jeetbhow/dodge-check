# Dodge Check

## About

Esports analytics is the application of data analysis and statistical methods to competitive video games. One of the problems in this domain is match outcome prediction. This involves using pre-game data to attempt to predict who will win. 

### What is this project? 

Dodge-Check helps you understand your chances of winning a League of Legends match before it even starts, based on which champions both teams picked.

### Why does it matter?

When you're in champion select for a ranked game, it's helpful to know if your team has a strong draft or if you're at a disadvantage. This tool analyzes the team compositions and gives you that insight - something that's actually useful for regular players, not just professionals or analysts.


# Technical Details

## Exploratory Data Analysis

The dataset that I used can be found on [Kaggle](https://www.kaggle.com/datasets/nathansmallcalder/lol-match-history-and-summoner-data-80k-matches). It contains about 148,000 ranked games of League of Legends. 

These are some key findings from the dataset. 

### Class Imbalance

In League of Legends there's something known as *blue-side advantage*. The blue team generally has a 1-3% advantage for various reasons:

- Blue side gets first pick which allows them to secure the strongest meta-defining champions before red side can respond. 
- Blue side has better access to the Rift Herald and Baron Nashor. 
- The game's default camera favours a bottom-left to top-right perspective. It makes it easier for players on the blue side to percieve skill shots because they'll generally be attacked from above.

![Charts depicting class imbalance in the dataset](./images/class-imbalance.png)


So we can see that the blue-side advantage in this particular dataset is 5 points. Despite that, this shouldn't really be an issue for the model. Here's why:

- There are a decent number of examples of both outcomes in the dataset. Class imbalance becomes problematic when there are extreme ratios, like 90-10 or 95-5. At this level it shouldn't affect the model's ability to learn patterns.
- Even if the model becomes slightly biased towards blue side, **that's how it actually is in league**. We wouldn't expect it to be unbiased.

### Elo Distribution

Master elo is overrepresented in the dataset. If we exclude it, then we get roughly a normal distribution.

- Most games are played in Gold, Platinum, Diamond, and Master elo. The number of games in the first 4 brackets are roughly equal. 
- Master elo has the most amount of games played. Challenger has the fewest.
- Unranked games made up about 15% of the dataset. They were removed from the overall analysis.

![Charts depicting elo distribution in dataset](./images/elo-distribution.png)

### Champion Analysis

The dataset includes all 172 champions in League of Legends, with pick rates ranging from 1.83% to 15.91%. Here are the key insights:

**Pick Rate Distribution:**
- The most popular champions are Kai'Sa (15.91%), Caitlyn (14.22%), Miss Fortune (13.80%), and Sylas (12.97%).
- 12 champions have pick rates above 10%, indicating a clear meta preference.
- The least picked champions include Skarner, Shyvana, Kalista, Rammus, and Nilah.
- All champions see meaningful play (no champion below 1% pick rate).

![Charts depicting champion pick frequencies in dataset](./images/champion-frequencies.png)


**Win Rate Analysis:**
- Champion win rates are well-balanced, averaging 49.96% with a median of 49.86%.
- Win rates range from 44.90% (Azir) to 52.30% (Kog'Maw), a relatively narrow spread.
- Top performers include Kog'Maw, Shen, Singed, Bel'Veth, Sona, Morgana, and Malphite.
- Bottom performers include Azir, K'Sante, Corki, Qiyana, Akali, and Zeri.

![Charts depicting champion winrates in dataset](./images/champion-winrates.png)


**Correlation Between Win Rate and Pick Rate:**
- High pick rate does not correlate with high win rate. Kai'Sa, despite being the most picked champion, maintains only a 49.99% win rate.
- Some niche champions like Kog'Maw and Singed show strong win rates despite lower pick rates, suggesting they excel in specific situations.
- The lack of correlation between popularity and performance indicates reasonable champion balance across the roster.

![Charts depicting scatter plot of winrate vs pickrate for champions](./images/champion-scatter-freq-vs-winrate.png)