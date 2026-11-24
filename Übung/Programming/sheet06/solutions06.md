# 1
...

# 2
The training error cannot choose 𝜆: 𝜆 =0 minimizes it, so it grows with 𝜆 for any data.
Choosing 𝜆 needs data that the weights were not fitted to.

# 3


# 4
Far from all training cars every 𝑘⁡(𝒙,𝒙𝑖)
is almost zero, so 𝑓⁡(𝒙) =∑𝑖𝛼𝑖 ⁢𝑘⁡(𝒙,𝒙𝑖)
is almost zero: the mean of the standardized training targets.

# 5

# 6
It stays about ±7
mpg wide: more cars pin down the function value 𝑓⁡(𝒙)
, but each car still scatters around it with the noise 𝜎
, which more data do not reduce.

# 7

# 8
𝑝⁡(𝒚 ∣𝑋)
is the density of the targets before any fitting: with a 5 hp kernel neighbouring cars are almost independent, so rough target vectors are as likely as the smooth observed one.