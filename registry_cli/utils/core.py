class Core:
    
    def print_table(self, headers, data):
        # Calculate column widths
        widths = [max(len(str(value)) for value in col) for col in zip(*data)]
        widths = [max(widths[i], len(headers[i])) for i in range(len(widths))]
        
        # Print header
        header = " | ".join(str(headers[i]).ljust(widths[i]) for i in range(len(headers)))
        print(header)
        print("-" * len(header))

        # Print data rows
        for row in data:
            print(" | ".join(str(row[i]).ljust(widths[i]) for i in range(len(row))))
