import scala.io.Source

@main def day2() =
    val source = Source.fromFile("input-02.txt")
    var safeReportCounter = 0

    for (line <- source.getLines())
        val numsLine = line.split(" ")
        val nums = numsLine.map(x => x.toInt)
        var safeReportFound = false
        for (i <- 0 to nums.length - 1)
            if (!safeReportFound)
                val currentNums = nums.zipWithIndex.collect { case (a, curi) if curi != i => a }
                if (reportSafe(currentNums))
                    safeReportCounter += 1
                    safeReportFound = true

    println(safeReportCounter)

def reportSafe(nums: Seq[Int]): Boolean =
    var increasingCorrectly = true
    var decreasingCorrectly = true
    for (i <- 0 to nums.length - 2)
      val diff = nums(i + 1) - nums(i)
      if (diff != 1 && diff != 2 && diff != 3) increasingCorrectly = false
      if (diff != -1 && diff != -2 && diff != -3) decreasingCorrectly = false
    increasingCorrectly || decreasingCorrectly
