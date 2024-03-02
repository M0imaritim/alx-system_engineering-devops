#!/usr/bin/env ruby
#accepts args and passess it to refular expression matching method
puts ARGV[0].scan(/hbt{2,5}n/).join

