# create via planck
# run via lumo?

(require '[planck.io :as io]
         '[planck.core :as core])

(def all-genome-file-slurped
  (core/slurp "./all-genomes-files.sh"))_

(def all-genome-file-io
  (io/line-seq "./all-genomes-files.sh"))_


