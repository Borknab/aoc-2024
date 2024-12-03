import scala.io.Source
import scala.util.matching.Regex
import scala.collection.mutable.ListBuffer

@main def day3() =
  val pattern: Regex = """mul\((\d+),(\d+)\)""".r
  val source = Source.fromFile("input-03.txt")
  var res = 0
  var totalLine = ""

  for (line <- source.getLines()) totalLine += line

  val lineCleaned = cleanLine(totalLine)
  val mults = pattern.findAllIn(lineCleaned).toList
  for (m <- mults)
    val numPattern: Regex = """(\d+)""".r
    val nums = numPattern.findAllIn(m).toList
    res += (nums(0).toInt * nums(1).toInt)

  println(res)

def cleanLine(line: String) =
  var i = 0
  var cleanedLine = ""
  var disabledParts: ListBuffer[Seq[Int]] = ListBuffer()
  var disabledStart = 0
  var disabledEnd = 0

  while (i < line.length)
    if (line.slice(i, i + 7) == "don't()")
      i = i + 7
      if (disabledStart == 0) disabledStart = i
    else if (line.slice(i, i + 4) == "do()" && disabledStart != 0)
      disabledParts.addOne(List(disabledStart, i))
      disabledStart = 0
      i = i + 4
    else
      i += 1
  if (disabledStart != 0) disabledParts.addOne(List(disabledStart, line.length))

  var start = 0
  for (part <- disabledParts)
    cleanedLine += line.slice(start, part(0))
    start = part(1)
  cleanedLine += line.slice(start, line.length)

  cleanedLine