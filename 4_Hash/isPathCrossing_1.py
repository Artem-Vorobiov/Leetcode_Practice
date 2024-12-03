class Solution:
    def isPathCrossing(self, path: str) -> bool:
        decoder = {
            'N' : 1,
            'S' : -1,
            'W' : -1,
            'E' : 1
        }

        coords = [0,0]
        log_file = {str(coords): 1}

        for step in path:
            if step == 'N' or step == 'S':
                coords[0] += decoder[step]
                if str(coords) not in log_file:
                    log_file[str(coords)] = 1
                else:
                    log_file[str(coords)] += 1
                    return True
            else:
                coords[1] += decoder[step]
                if str(coords) not in log_file:
                    log_file[str(coords)] = 1
                else:
                    log_file[str(coords)] += 1
                    return True
        return False

