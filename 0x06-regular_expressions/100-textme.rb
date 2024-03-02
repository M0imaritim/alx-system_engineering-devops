#!/usr/bin/env ruby
#output: [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
