
## Question 5
**a) What were the engineering advances that led to Deep Blue's success? Which of them can be transferred to other problems, 
and which are specific to chess?**

Deep Blue's victory over Garry Kasparov in 1997 came from several key engineering advancements. One major improvement was the 
enhanced chess chips in Deep Blue II. These chips had a completely redesigned evaluation function, increasing the number of 
features analyzed from about 6,400 to over 8,000. This focus on refining evaluation functions can be applied to many fields, 
like machine learning and AI, where better feature analysis leads to improved performance.

Another important change was the increase in processing power. The number of chess chips was more than doubled, and a newer, 
more powerful computer supported this upgrade, significantly boosting processing speed. This principle of scaling up processing 
capabilities is useful in various tech problems, especially in areas where fast data processing is crucial.

Additionally, the team developed software tools for debugging and preparation, which helped tune evaluations and visualize performance. 
These tools made it easier to prepare for matches and can be valuable in software development and project management across many 
industries.

Lastly, the new chips included specialized move generation features, like hardware repetition detection. While these enhancements
optimized gameplay specifically for chess, the idea of optimizing operations can also apply to other strategic simulations. 

**b) AlphaZero is compared to a number of modern game-playing programs, such as StockFish, which work similarly to Deep Blue. 
The paper shows that AlphaZero is able to defeat StockFish even when it is given only 1/100 of the computing time. Why is that? 
Please frame your answer in terms of search and the number of nodes evaluated.**

AlphaZero beats Stockfish even with just 1/100 of the computing time because of how it searches and evaluates moves. 
Unlike Stockfish, which uses a super-fast alpha-beta search to check millions of positions, AlphaZero relies on a Monte Carlo 
tree search (MCTS) guided by a deep neural network.

Stockfish evaluates around 70 million positions per second using carefully crafted rules that experts have fine-tuned over 
the years. While this works well, it can struggle in complex situations where deeper understanding is needed.

On the other hand, AlphaZero searches only about 80,000 positions per second, but it focuses on the best moves by predicting 
which ones are most likely to succeed. Its neural network learns from self-play, so it develops a sense of strategy and patterns 
in the game. This means AlphaZero doesn't just know the rules; it has a deeper understanding of the game.

So, even though AlphaZero looks at way fewer positions, it’s making smarter evaluations. This ability to focus on quality over 
quantity lets it play at a superhuman level with much less computing power.


