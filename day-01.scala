import scala.io.Source
import scala.collection.mutable

@main def hello() =
    val source = Source.fromFile("input-01.txt")
    var firstNums: mutable.ListBuffer[Int] = mutable.ListBuffer()
    var secondNums: mutable.ListBuffer[Int] = mutable.ListBuffer()

    for (line <- source.getLines())
        val nums = line.split(" ")
        val num1 = nums.head.toInt
        val num2 = nums(nums.length - 1).toInt
        firstNums += num1
        secondNums += num2

    firstNums = firstNums.sorted
    secondNums = secondNums.sorted
    var totalDistance = 0
    firstNums.zip(secondNums).map((num1, num2) => {
       totalDistance += math.abs(num1 - num2) 
    })
    
    // Part 1
    println(s"Part 1: ${totalDistance}")
    
    // Part 2
    var numSet = firstNums.toSet
    var leftNumCounter: mutable.Map[Int, Int] = mutable.Map()
    for (num <- secondNums)
        if (numSet.contains(num))
            val currentCount = leftNumCounter.getOrElse(num, 0)
            leftNumCounter.put(num, currentCount + 1)
            
    var similarity = 0
    firstNums.foreach(x => {
        val count = leftNumCounter.getOrElse(x, 0)
        similarity += x * count
    })
    println(s"Part 2: ${similarity}")