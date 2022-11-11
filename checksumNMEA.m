function check = checksumNMEA(line)
% function check = checksumNMEA(line)
%
% This function receives a line of data in NMEA format and returns true if
% the checksum is correct and false if it is not.


% check the correct character for line starting
if line(1) == '$'
    % checksum starts after a star symbol (*)
    position_star = strfind(line,'*');
    % bit-wise XOR of the line between $ and *
    checksum = 0;
    for jj = 2:position_star-1
        checksum = bitxor(checksum,double(line(jj)));
    end
    % convert to hexadecimal, add a 0 if only has one character
    checksum = char(dec2hex(checksum));
    if length(checksum) == 1
        checksum = ['0' checksum];     
    end
    % checksum comparison
    if checksum == line(position_star+1:position_star+2)
        check = true;
    else
        check = false;
    end
else
    check = false;
end

