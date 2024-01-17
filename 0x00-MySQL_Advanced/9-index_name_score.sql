-- Script to creates an index idx_name_first_score on table
CREATE INDEX idx_name_first_score on names(name(1), score)
