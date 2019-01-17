esearch -db protein -query "$@"|efetch -format fasta > $@.fas
