#!/usr/bin/env python3

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

at_index_location = data.find('@')

empty_space_after_at = data.find(' ',at_index_location) # find has 3 params. 1. Substring
                                                        # 2. start, 3. end. We are only
                                                        # passing substring and start, not end

host_name = data[at_index_location+1 : empty_space_after_at]

print(host_name)

