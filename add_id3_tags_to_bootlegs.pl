#!/usr/bin/perl -w

$artist = <>;
$date = <>;
$place = <>;
$city = <>;
chomp($artist);
chomp($date);
chomp($place);
chomp($city);

$artist =~ s/\r//g;
$album = "$date $place $city";
$album =~ s/\r//g;
$album =~ s/\n//g;

while(<>) {
    chomp;
    s/\r//;
    if (/(\d\d)  (.*)/) {
	print "eyeD3  -n $1 -a \"$artist\" -A \"$album\" -t \"$2\" *$1.mp3\n";
	print "mv *$1.mp3 \"$1 - $2.mp3\"\n";
    }
}

