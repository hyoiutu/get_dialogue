#!/bin/bash

input_result=$(du dialogue_data/input*)
output_result=$(du dialogue_data/output*)

while read file_size file_name
do
   if [ ! $file_size = 0 ]; then
     cat $file_name >> input.dat
   fi
done <<END
$input_result
END
while read file_size file_name
do
   if [ ! $file_size = 0 ]; then
     cat $file_name >> output.dat
   fi
done <<END
$output_result
END
