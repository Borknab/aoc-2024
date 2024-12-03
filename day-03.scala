import scala.io.Source
import scala.util.matching.Regex

@main def day3() =
  val pattern: Regex = """mul\((\d+),(\d+)\)""".r
  val source = Source.fromFile("input-03.txt")
  var res = 0

  for (line <- source.getLines())
    val lineCleaned = cleanLine(line)
    val mults = pattern.findAllIn(lineCleaned).toList
    for (m <- mults)
      val numPattern: Regex = """(\d+)""".r
      val nums = numPattern.findAllIn(m).toList
      res += (nums(0).toInt * nums(1).toInt)

  println(res)

def cleanLine(line: String) =
  var i = 0
  while (i < line.length)
    if (line.slice(i, i + 4) == "do()")
