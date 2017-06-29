module Project1 where

threeAndFive :: Integer -> [Integer]
threeAndFive x = case mod x 3 == 0 || mod x 5 == 0 of
    True -> x : threeAndFive (x + 1)
    False -> threeAndFive (x + 1)

main :: IO ()
main = do
    print . sum . takeWhile (< 1000) $ threeAndFive 1
