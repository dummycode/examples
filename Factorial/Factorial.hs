import Text.Read

main = do
    putStr "Enter number: "
    number <- getLine
    putStrLn $ show $ factorial (readMaybe number :: Maybe Integer)

factorial :: (Maybe Integer) -> Integer
factorial Nothing = 0
factorial (Just n) = product [1..n]
