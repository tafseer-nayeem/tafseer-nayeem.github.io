const table = document.querySelector('#model-leaderboard');

if (table) {
  const headers = [...table.tHead.rows[0].cells];
  const body = table.tBodies[0];
  let activeSort = 'composite';
  let descending = true;

  headers.forEach((header, column) => {
    const button = header.querySelector('button');
    button.addEventListener('click', () => {
      const sort = button.dataset.sort;
      descending = sort === activeSort ? !descending : sort !== 'rank' && sort !== 'model';
      activeSort = sort;

      const rows = [...body.rows];
      rows.sort((a, b) => {
        const first = sort === 'rank' ? Number(a.dataset.rank) : sort === 'model' ? a.cells[1].textContent.trim() : Number(a.cells[column].textContent);
        const second = sort === 'rank' ? Number(b.dataset.rank) : sort === 'model' ? b.cells[1].textContent.trim() : Number(b.cells[column].textContent);
        const comparison = typeof first === 'string' ? first.localeCompare(second) : first - second;
        return (descending ? -comparison : comparison) || Number(a.dataset.rank) - Number(b.dataset.rank);
      });
      body.replaceChildren(...rows);

      headers.forEach((item) => {
        item.removeAttribute('aria-sort');
        item.querySelector('.sort-indicator')?.remove();
      });
      header.setAttribute('aria-sort', descending ? 'descending' : 'ascending');
      const indicator = document.createElement('span');
      indicator.className = 'sort-indicator';
      indicator.setAttribute('aria-hidden', 'true');
      indicator.textContent = descending ? ' \u25bc' : ' \u25b2';
      button.append(indicator);
    });
  });
}
