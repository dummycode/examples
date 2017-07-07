import Data.Time.Calendar
import Data.Time.Calendar.WeekDate

main :: IO ()
main = print . length . filter isSunday . map toWeekDate . firstOfMonths (fromGregorian 1901 1 1) $ (fromGregorian 2000 12 31)

isSunday :: (Integer, Int, Int) -> Bool
isSunday (_, _, d) = d == 7

firstOfMonths :: Day -> Day -> [Day]
firstOfMonths current end = if current > end then [] else current : firstOfMonths (addGregorianMonthsClip 1 current) end
