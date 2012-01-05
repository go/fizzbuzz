#!/usr/bin/env perl

sub check_number {
  my $end = @_[0];

  for ($xx = 1; $xx <= $end; $xx++) {
    if ($xx%15 == 0){
      print "FizzBuzz\n";
    }
    elsif ($xx%3 == 0){
      print "Fizz\n";
    }
    elsif ($xx%5 == 0){
      print "Buzz\n";
    }
    else {
      print "$xx\n";
    }
  }
}

if (@ARGV < 1){
  die("Please give an argument number\n");
}
else {
  $end = $ARGV[0];
}

&check_number($end);
